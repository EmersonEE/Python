import pywhatkit 

def send_whatsapp_message(phone_number, message):
    """
    Sends a WhatsApp message to a specified phone number.
    
    Parameters:
    phone_number (str): The phone number in the format 'country_code-phone_number'.
    message (str): The message to be sent.
    
    Returns:
    None
    """
    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        print(f"Message sent to {phone_number}: {message}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    phone_number = input("Enter the phone number (format: 'country_code-phone_number'): ")
    message = input("Enter the message to send: ")
    send_whatsapp_message(phone_number, message)
# Example usage:
# send_whatsapp_message("+50249964191", "Hello, this is a test message!")
# Note: Ensure you have the necessary permissions and that the phone number is valid.
# Example usage:
# send_whatsapp_message("+1234567890", "Hello, this is a test message!")        