from selenium.webdriver.common.by import By
import time
from getting_data import from_data, to_data  # Assuming from_data and to_data come from getting_data module
import get_flight_data_for_20_days  # Import the next test case


def main(driver):
    try:
        # Ensure that the driver is not None before attempting to find the element
        if driver is None:
            raise ValueError("Driver instance is None. Please provide a valid WebDriver instance.")

        # Find and click the close button (if modal is present)
        close_button = driver.find_element(By.XPATH, '//span[@class="commonModal__close"]')
        close_button.click()
        time.sleep(2)  # Delay for observation
        print("Data window closed successfully.")

        # Proceed with flight data input after closing the modal
        try:
            # One-way trip
            driver.find_element(By.XPATH, "//li[@data-cy='oneWayTrip']").click()
            time.sleep(2)
            print("One-way trip selected.")

        except Exception as e:
            print(f"An error occurred while selecting the one-way trip: {e}")

        try:
            # From city
            time.sleep(2)
            driver.find_element(By.XPATH, "//input[@id='fromCity']").click()
            time.sleep(2)
            from_input_element = driver.find_element(By.XPATH, "//input[@aria-controls='react-autowhatever-1']")
            time.sleep(2)
            from_input_element.send_keys(from_data)  # Use the 'from_data' value from your getting_data module
            time.sleep(2)
            driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']").click()
            print(f"From city {from_data} selected.")

        except Exception as e:
            print(f"An error occurred while entering the 'From' city: {e}")

        try:
            # To city
            driver.find_element(By.XPATH, "//input[@id='toCity']").click()
            time.sleep(2)
            to_input_element = driver.find_element(By.XPATH, "//input[@aria-controls='react-autowhatever-1']")
            time.sleep(2)
            to_input_element.send_keys(to_data)  # Use the 'to_data' value from your getting_data module
            time.sleep(2)
            driver.find_element(By.XPATH, "//li[@id='react-autowhatever-1-section-0-item-0']").click()
            time.sleep(2)

            print(f"To city {to_data} selected.")

        except Exception as e:
            print(f"An error occurred while entering the 'To' city: {e}")

        try:
            # Date selection and search
            driver.find_element(By.XPATH, "//div[@class='DayPicker-Day DayPicker-Day--selected']").click()
            driver.find_element(By.XPATH,
                                "//a[@class='primaryBtn font24 latoBold widgetSearchBtn ' and text()='Search']").click()
            print("Search button clicked.")
            time.sleep(5)  # Optional delay for observing results

        except Exception as e:
            print(f"An error occurred while selecting the date or clicking search: {e}")


# After search button is clicked, run the next script to fetch flight data for 20 days
        print("Running get_flight_data_for_20_days.py...")
        get_flight_data_for_20_days.main(driver)  # Pass the driver to the next script
    except Exception as e:
        print(f"An error occurred: {e}")
        # Prevent browser closure on error by catching the exception and handling it gracefully



# If this script is executed directly, driver is expected to be provided from another module/script
if __name__ == "__main__":
    driver = None  # This should be replaced by a valid driver instance for testing purposes
    main(driver)
