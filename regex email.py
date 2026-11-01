
import re

# Input text
text = input("Enter the text: ")

# Regular expression to find email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses
emails = re.findall(pattern, text)

# Display results
if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email addresses found.")
