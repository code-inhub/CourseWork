
import re

def validate_name(name):
    # Validate the user name
    if len(name) == 0 or len(name) > 15:
        return False
    if not name.isalpha():
        return False
    return True

def validate_phone_no(phoneno):
    # Validate the phone number
    if not (len(phoneno) == 10 and phoneno.isdigit()):
        return False
    if len(set(phoneno)) == 1:
        return False
    return True

def validate_email_id(email_id):
    # Validate the email ID
    email_pattern = r'^[a-zA-Z0-9._%+-]+@(gmail|yahoo|hotmail)\.com$'
    if re.match(email_pattern, email_id):
        return True
    return False

# Testing the functions
def main():
    name = input("Enter your name: ")
    phoneno = input("Enter your phone number: ")
    email_id = input("Enter your email ID: ")

    print(f"Is name '{name}' valid?\n {validate_name(name)}")
    print(f"Is phone number '{phoneno}' valid?\n {validate_phone_no(phoneno)}")
    print(f"Is email ID '{email_id}' valid?\n {validate_email_id(email_id)}")

if __name__ == "__main__":
    main()
