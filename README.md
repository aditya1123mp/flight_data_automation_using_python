This project automates the process of gathering flight data from MakeMyTrip. It prompts the user for the source and destination cities, along with an email address, then retrieves the data for the next 20 days and sends it in both Excel and TXT formats to the provided email.

 Project Overview

This automation tool collects flight information from the MakeMyTrip website for a specified route. It extracts key details for the next 20 days and emails the compiled data in two formats: Excel and TXT.

Features

- User Input: Prompt for source and destination cities, as well as the recipient's email address.
- Flight Data Collection: Scrapes MakeMyTrip for the latest flight data over the next 20 days.
- Data Output: Generates an Excel file and a TXT file containing the flight data.
- Email Automation: Sends both files to the specified email address.

 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```

3. Install required packages:
   - Install Python packages for web scraping, file handling, and email automation:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Email Settings:
   - In the script, update the email settings (e.g., SMTP server, email credentials) as required.

Usage

1. Run the Script:
   - Start the program with:
   ```bash
   python main.py
   ```

2. Provide User Input:
   - Select source and destination cities from the list provided.
   - Enter the email address where the data will be sent.

3. Receive Email:
   - After processing, check your email for the Excel and TXT files containing the requested flight data.

Requirements

- Python
- Required libraries (see `requirements.txt`)

Example

Input:
   ```
   Source City: Delhi (DEL)
   Destination City: Mumbai (BOM)
   Email: user@example.com
   ```

Output:
   - An email containing `flight_data.xlsx` and `flight_data.txt` with flight details from Delhi to Mumbai for the next 20 days.

Contributing

Feel free to submit pull requests for improvements or additional features. Please ensure that any contributions adhere to the project’s code and style guidelines.
