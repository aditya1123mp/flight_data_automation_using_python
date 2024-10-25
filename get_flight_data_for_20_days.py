from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime, timedelta
from getting_data import to_data, from_data

def main(driver):
    # Specify the absolute path to save the file
    file_path = r'C:\Users\DELL\OneDrive\Desktop\Flight_Details_make_my_trip.txt'
    file = open(file_path, "w", encoding="utf-8")

    base_url = f"https://www.makemytrip.com/flight/search?itinerary={from_data}-{to_data}-"
    suffix_url = "&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng"
    today = datetime.now()

    try:
        # Loop for the next 20 days
        for i in range(20):
            future_date = today + timedelta(days=i)
            formatted_date = future_date.strftime('%d/%m/%Y')
            dynamic_url = base_url + formatted_date + suffix_url
            driver.get(dynamic_url)
            time.sleep(5)  # Allow time for the page to load

            button_primary_xpath = "//span[@class='button buttonPrimary pushRight widthFitContent' and text()='GOT IT']"
            button_okay_xpath = "//button[@class='button buttonSecondry buttonBig fontSize12 relative' and text()='OKAY, GOT IT!']"
            no_flights_error_xpath = "//p[@class='error-title' and text()='No Flights Found']"
            listing_card_xpath = "//div[@class='listingCard  appendBottom5']"
            overlay_xpath = "//div[@class='coachmarkOverlay']"

            try:
                # Wait for the overlay to disappear
                WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, overlay_xpath)))
            except TimeoutException:
                print("Overlay did not disappear in time")

            # Check and click on "OKAY, GOT IT!" or "GOT IT" buttons if they are present
            try:
                button_okay = driver.find_element(By.XPATH, button_okay_xpath)
                button_okay.click()
                time.sleep(2)
                print(f"Clicked on 'OKAY, GOT IT!' for date: {formatted_date}")
                time.sleep(2)
            except NoSuchElementException:
                try:
                    button_primary = driver.find_element(By.XPATH, button_primary_xpath)
                    button_primary.click()
                    time.sleep(2)
                    print(f"Clicked on 'GOT IT' for date: {formatted_date}")
                    time.sleep(2)
                except NoSuchElementException:
                    print(f"No pop-up buttons found for date: {formatted_date}")

            # Continue with the rest of your logic...
            try:
                listings = driver.find_elements(By.XPATH, listing_card_xpath)
                if listings:
                    print(f"Listings found for date: {formatted_date}")
                    for listing in listings:
                        flight_name = listing.find_element(By.XPATH, ".//div/p[@class='boldFont blackText airlineName']").text
                        flight_id = listing.find_element(By.XPATH, ".//div/p[@class='fliCode']").text
                        departure_time = listing.find_element(By.XPATH, ".//div[@class='flexOne timeInfoLeft']/p[@class='appendBottom2 flightTimeInfo']").text
                        arrival_time = listing.find_element(By.XPATH, ".//div[@class='flexOne timeInfoRight']/p[@class='appendBottom2 flightTimeInfo']").text
                        total_time = listing.find_element(By.XPATH, ".//div[@class='stop-info flexOne']").text
                        price = listing.find_element(By.XPATH, ".//div[@class='blackText fontSize18 blackFont white-space-no-wrap clusterViewPrice']/span").text
                        departure_airport = listing.find_element(By.XPATH, ".//div[@class='flexOne timeInfoLeft']/p[@class='blackText']").text
                        arrival_airport = listing.find_element(By.XPATH, ".//div[@class='flexOne timeInfoRight']/p[@class='blackText']").text

                        offer_details = (f"Date: {formatted_date}\n"
                                         f"Flight Name: {flight_name}\n"
                                         f"Flight ID: {flight_id}\n"
                                         f"Price: {price}\n"
                                         f"Departure Airport: {departure_airport}\n"
                                         f"Arrival Airport: {arrival_airport}\n"
                                         f"Total Time: {total_time}\n"
                                         f"Departure Time: {departure_time}\n"
                                         f"Arrival Time: {arrival_time}\n"
                                         "--------------------------------------------------------\n")

                        print(offer_details)
                        file.write(offer_details)
                else:
                    print(f"No listings found for date: {formatted_date}. Trying the next date.")
            except NoSuchElementException:
                print(f"No listings found for date: {formatted_date}. Trying the next date.")
    finally:
        file.close()
