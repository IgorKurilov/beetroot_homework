def is_valid_phone_number(phone_number):
    # Check if the phone number contains only numerical characters
    if not phone_number.isdigit():
        return False
    
    # Check if the length of the phone number is 10 characters
    if len(phone_number) != 10:
        return False
    
    return True


# Test the function with sample phone numbers
phone_numbers = ["1234567890", "abcdefghij", "123456789", "12345678901"]
for number in phone_numbers:
    if is_valid_phone_number(number):
        print(f"The phone number '{number}' is valid.")
    else:
        print(f"The phone number '{number}' is invalid.")