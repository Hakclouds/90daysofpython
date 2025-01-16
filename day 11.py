import re

# Define the regex pattern
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Function to validate an email
def validate_email(email):
    if re.match(email_regex, email):
        print("You entered a valid email address, congratulation")
    else:
        print("Try again. The email provided is not correct")

email = input("Please enter your correct email for validation: ")

validate_email(email)

# Test the function
# emails = [
#     "valid.email@example.com",
#     "invalid-email.com",
#     "username@.com",
#     "user@domain",
#     "user@domain.c",
#     "user@domain.toolongextension",
# ]
#
# for email in emails:
#     print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")
