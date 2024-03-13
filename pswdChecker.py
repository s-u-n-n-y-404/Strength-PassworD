import re

def password_strength(password):
    """Check the strength of a password."""
    # Define criteria for a strong password
    length_regex = re.compile(r'.{8,}')
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')
    special_char_regex = re.compile(r'[^a-zA-Z0-9]')

    # Check if password meets each criterion
    length_ok = bool(length_regex.search(password))
    uppercase_ok = bool(uppercase_regex.search(password))
    lowercase_ok = bool(lowercase_regex.search(password))
    digit_ok = bool(digit_regex.search(password))
    special_char_ok = bool(special_char_regex.search(password))

    # Calculate overall strength score
    strength_score = sum([length_ok, uppercase_ok, lowercase_ok, digit_ok, special_char_ok])

    # Determine the strength level
    if strength_score == 5:
        return "Very strong"
    elif strength_score >= 3:
        return "Strong"
    elif strength_score >= 2:
        return "Moderate"
    elif strength_score >= 1:
        return "Weak"
    else:
        return "Very weak"

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = password_strength(password)
    print("Password strength:", strength)
  
