import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import exists
from getting_data import email_data, from_data, to_data

def main():
    # Define email credentials
    username = ''  # Replace with your Gmail address
    password = ''  # Replace with your Gmail app password
    recipient_email = email_data  # Recipient email

    # Define email properties for Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Use 465 for SSL or 587 for TLS

    try:
        # Create a default MIMEMultipart object
        message = MIMEMultipart()
        message['From'] = username
        message['To'] = recipient_email
        message['Subject'] = f"Latest Automation Run: Flight Data for {from_data} to {to_data}"

        # Create the message body
        email_body = (
            f'Please find the attached test results from the latest automation run for flight data from {from_data} to {to_data}.\n\n'
            'Check project details on GitHub: https://github.com/aditya1123mp/make_my_trip_flight_data_automation'
        )
        message.attach(MIMEText(email_body, 'plain'))

        # Attach files
        filenames = [
            'C:\\Users\\DELL\\OneDrive\\Desktop\\Flight_Details_make_my_trip_data.xlsx',
            'C:\\Users\\DELL\\OneDrive\\Desktop\\Flight_Details_make_my_trip.txt'
        ]

        for filename in filenames:
            if exists(filename):
                with open(filename, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={filename.split("/")[-1]}')
                    message.attach(part)
                print(f'Attached file: {filename.split("/")[-1]}')
            else:
                print(f'File not found or inaccessible: {filename}')

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(username, recipient_email, message.as_string())

        print('Email sent successfully!')

    except Exception as e:
        print(f'Failed to send the email: {e}')

if __name__ == "__main__":
    main()
