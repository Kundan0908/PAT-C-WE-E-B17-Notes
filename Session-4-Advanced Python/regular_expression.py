# A RegEx or Regular Expression is a sequence or character that forms a search pattern.
# Import the re module to start using regex expressions.

import re

# print(re.search('n','kundan'))

def validate_pancard(pancard_no):
    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"
    if re.match(pattern, pancard_no):
        return True
    else:
        return False

print(validate_pancard("BAJPC4350M"))

