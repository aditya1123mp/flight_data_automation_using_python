import customtkinter as ctk
import tkinter.messagebox as tkmb

# Selecting GUI theme - dark, light, system (for system default)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x500")
app.title("Modern UI - From, To & Email Address")

# Global variables to store user input data
from_data = ""
to_data = ""
email_data = ""

# List of destinations
destinations = [
    "Agartala (IXA)", "Aizawl (AJL)", "Bagdogra (IXB)", "Agatti (AGX)", "Amritsar (ATQ)",
    "Bareilly (BEK)", "Agra (AGR)", "Ahmedabad (AMD)", "Aurangabad (IXU)", "Ayodhya (AYJ)",
    "Belagavi (IXG)", "Bengaluru (BLR)", "Bhopal (BHO)", "Bhubaneswar (BBI)", "Chandigarh (IXC)",
    "Chennai (MAA)", "Coimbatore (CJB)", "Darbhanga (DBR)", "Dehradun (DED)", "Deoghar (DGH)",
    "Dharamshala (DHM)", "Diu (DIU)", "Gondia (GDB)", "Durgapur (RDP)", "Gaya (GAY)", "Dibrugarh (DIB)",
    "Delhi (DEL)", "Dimapur (DMU)", "Goa (GOI)", "Gorakhpur (GOP)", "Guwahati (GAU)", "Gwalior (GWL)",
    "Hirasar (HSR)", "Hubli (HBX)", "Hyderabad (HYD)", "Imphal (IMF)", "Indore (IDR)", "Itanagar (HGI)",
    "Jabalpur (JLR)", "Jagdalpur (JGB)", "Jaipur (JAI)", "Jaisalmer (JSA)", "Jammu (IXJ)", "Jodhpur (JDH)",
    "Jorhat (JRH)", "Kadapa (CDP)", "Jharsuguda (JRG)", "Kannur (CNN)", "Kanpur (KNU)", "Khajuraho (HJR)",
    "Kochi (COK)", "Kolkata (CCU)", "Kozhikode (CCJ)", "Kurnool (KJB)", "Lucknow (LKO)", "Madurai (IXM)",
    "Mysuru (MYQ)", "Nagpur (NAG)", "Nashik (ISK)", "Pantnagar (PGH)", "Patna (PAT)", "Port Blair (IXZ)",
    "Mangaluru (IXE)", "Kolhapur (KLH)", "Leh (IXL)", "Mumbai (BOM)", "North Goa (GOX)", "Prayagraj (IXD)",
    "Pune (PNQ)", "Raipur (RPR)", "Rajahmundry (RJA)", "Rajkot (RAJ)", "Ranchi (IXR)", "Salem (SXV)",
    "Shillong (SHL)", "Shirdi (SAG)", "Shivamogga (RQY)", "Silchar (IXS)", "Srinagar (SXR)", "Surat (STV)",
    "Thiruvananthapuram (TRV)", "Tiruchirappalli (TRZ)", "Tirupati (TIR)", "Vadodara (BDQ)", "Varanasi (VNS)",
    "Tuticorin (TCR)", "Vijayawada (VGA)", "Udaipur (UDR)", "Visakhapatnam (VTZ)"
]


def submit_data():
    global from_data, to_data, email_data  # Declare global variables to update them here

    # Get selected data and extract the airport codes
    from_data = from_combobox.get().split()[-1].strip("()")  # Extracts "IXA" from "Agartala (IXA)"
    to_data = to_combobox.get().split()[-1].strip("()")  # Extracts "BOM" from "Mumbai (BOM)"
    email_data = email_entry.get()

    # Validate if all fields are filled
    if from_data and to_data and email_data:
        # Show success message if all fields are filled
        tkmb.showinfo(title="Data Submitted", message="Your data has been successfully submitted")
        print(f"From: {from_data}")  # Only the code like 'DEL'
        print(f"To: {to_data}")
        print(f"Email: {email_data}")
        app.destroy()  # Close the main window after submission
    else:
        # Show error message if any field is empty
        tkmb.showerror(title="Submission Failed", message="All fields are required!")


# Main UI layout
label = ctk.CTkLabel(app, text="This is the main UI page")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Enter the Details Below:')
label.pack(pady=12, padx=10)

# 'From' Combobox
from_combobox = ctk.CTkComboBox(master=frame, values=destinations, width=300)
from_combobox.set("Select From")  # Placeholder
from_combobox.pack(pady=20, padx=10)

# 'To' Combobox
to_combobox = ctk.CTkComboBox(master=frame, values=destinations, width=300)
to_combobox.set("Select To")  # Placeholder
to_combobox.pack(pady=12, padx=10)

# Email Entry
email_entry = ctk.CTkEntry(master=frame, placeholder_text="Email Address", width=300)
email_entry.pack(pady=12, padx=10)

# Submit Button
button = ctk.CTkButton(master=frame, text='Submit', command=submit_data)
button.pack(pady=12, padx=10)

app.mainloop()

def main():
    if __name__ == "__main__":
        main()