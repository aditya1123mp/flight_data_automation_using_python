import access_makemytrip_site
#import get_flight_data_for_20_days
import input_flight_data
import getting_data
import save_data_in_excel
import send_email
def run_all_scripts():
    # Run the 'getting_data' test case (this is working fine)
    print("Running getting data...")
    getting_data.main()  # Assuming getting_data has a main() function

    # Run 'access_makemytrip_site' test case to open the website
    print("Running access_makemytrip_site.py...")
    driver = access_makemytrip_site.main()  # Call the main() from access_makemytrip_site

    # Run 'input_flight_data' to check and input the data
    print("Running input_flight_data.py...")
    input_flight_data.main(driver)  # Pass the driver instance to input_flight_data

    # Now that the search button is clicked, run 'get_flight_data_for_20_days'
#    print("Running get_flight_data_for_20_days.py...")
#    get_flight_data_for_20_days.main(driver)  # Pass the driver instance

    # Optionally, save the flight data in Excel
    print("Running save_data_in_excel.py...")
    save_data_in_excel.main()

    # Optionally, save the flight data in Excel
    print("Running send_email.py...")
    send_email.main()



if __name__ == "__main__":
    run_all_scripts()