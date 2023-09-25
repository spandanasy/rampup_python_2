import re

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

with open('email_txt_file.txt', 'r',  encoding='utf-8') as file:
    text = file.read()

email_addresses = re.findall(email_pattern, text)

for email in email_addresses:
    print(email)
