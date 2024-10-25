from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_case_to_close_the_data_window
import test_case_to_input_data_in_data_fileds

def main(driver):
    try:
        # Wait for the close button to be present (maximum wait of 10 seconds)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='commonModal__close']"))
        )
        # If the close button is found, close the data window
        print("Closing the data window...")
        test_case_to_close_the_data_window.main(driver)
    except NoSuchElementException:
        print("Close button not found, proceeding to input data...")
        # If the close button is not found, input data in fields
        test_case_to_input_data_in_data_fileds.main(driver)
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        # Optionally, prevent browser closure if needed after an exception
        driver.save_screenshot('error_screenshot.png')  # To help debugging
        raise e  # Re-raise the exception to propagate it upwards if necessary

# No need to add driver initialization here, as it is passed from 'fulltestcase.py'
