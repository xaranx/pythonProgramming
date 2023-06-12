# regular expression 
# Regex
import re

email = input("What's your Email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#    print("Valid")
# else:
#    print("Invalid")

if re.search(r"^[^@]+@[^@]+\.edu$", email): 
    print("Valid")
else:
    print("Invalid")



