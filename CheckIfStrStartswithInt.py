import re

# String
my_string = "houses90 90"

# Search if start with a number
reg = re.search('^\s*[0-9]',my_string)

# Print result
print(reg)