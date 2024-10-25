from selenium.webdriver.common.by import By
import time
from getting_data import from_data, to_data
import get_flight_data_for_20_days  # Import the next test case


def main(driver):
    try:
        # One-way trip
        driver.find_element(By.XPATH, '//li[@data-cy="oneWayTrip"]').click()
        time.sleep(2)

        # From city
        driver.find_element(By.XPATH, '//input[@id="fromCity"]').click()
        time.sleep(2)
        from_input = driver.find_element(By.XPATH, '//input[@aria-controls="react-autowhatever-1"]')
        time.sleep(2)
        from_input.send_keys(from_data)
        time.sleep(2)
        driver.find_element(By.XPATH, '//li[@id="react-autowhatever-1-section-0-item-0"]').click()
        time.sleep(2)

        # To city
        driver.find_element(By.XPATH, '//input[@id="toCity"]').click()
        time.sleep(2)
        to_input = driver.find_element(By.XPATH, '//input[@aria-controls="react-autowhatever-1"]')
        time.sleep(2)
        to_input.send_keys(to_data)
        time.sleep(2)
        driver.find_element(By.XPATH, '//li[@id="react-autowhatever-1-section-0-item-0"]').click()
        time.sleep(2)

        # Date selection and search
        driver.find_element(By.XPATH, '//div[@class="DayPicker-Day DayPicker-Day--selected"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//a[@class="primaryBtn font24 latoBold widgetSearchBtn " and text()="Search"]').click()

        time.sleep(5)  # Optional delay for observing results
        # After search button is clicked, run the next script to fetch flight data for 20 days
        print("Running get_flight_data_for_20_days.py...")
        get_flight_data_for_20_days.main(driver)  # Pass the driver to the next script

    except Exception as e:
        print(f"An error occurred while entering flight data: {e}")

if __name__ == "__main__":
    driver = None  # Replace with a valid driver instance for testing
    main(driver)
