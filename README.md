# Strength-PassworD
A simple example of a cyber security project using Python that checks the strength of passwords!


# Explanation:

1. The password_strength function checks various criteria to determine the strength of a password.
2. Regular expressions are used to define the criteria:
   - length_regex checks if the password is at least 8 characters long.
   - uppercase_regex, lowercase_regex, digit_regex, and special_char_regex check for the presence of uppercase letters, lowercase letters, digits, and special characters, respectively.
3. Each criterion is checked using the search method of the regular expression object, and the result is converted to a boolean (True if found, False otherwise).
4. The strength score is calculated based on how many criteria the password meets.
5. The overall strength level is determined based on the strength score.
6. In the example usage, the user is prompted to enter a password, and the strength of the password is displayed.

# This project helps users evaluate the strength of their passwords and encourages them to use stronger passwords for better cybersecurity.
