import re

def validate_indian_mobile_number(number):
    """
    Validates an Indian mobile number.
    Assumes a 10-digit number starting with 6, 7, 8, or 9.
    Optionally allows for +91 or 91 prefix.
    """
    if re.fullmatch(r"^((\+91|91)?\s?[6-9]\d{9})$", number):
        return True
    else:
        return False

# Test cases
print(f"9876543210 is valid: {validate_indian_mobile_number('9876543210')}")
print(f"+919876543210 is valid: {validate_indian_mobile_number('+919876543210')}")
print(f"91 9876543210 is valid: {validate_indian_mobile_number('91 9876543210')}")
print(f"5123456789 is valid: {validate_indian_mobile_number('5123456789')}")
print(f"987654321 is valid: {validate_indian_mobile_number('987654321')}")
print(f"abc9876543210 is valid: {validate_indian_mobile_number('abc9876543210')}")