import re
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
url_regex = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
phone_regex = r"^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
credit_card_regex = r"^(?:\d{4}[- ]?){3}\d{4}$"

def is_valid_email(email):
    return re.match(email_regex, email) 
def is_valid_url(url):
    return re.match(url_regex, url) 
def is_valid_phone(phone):
    return re.match(phone_regex, phone) 
def is_valid_credit_card(card_number):
    return re.match(credit_card_regex, card_number) 


# Test samples
emails = ["user@example.com", "firstname.lastname@company.co.uk"]
urls = ["https://www.example.com", "https://subdomain.example.org/page"]
phones = ["(123) 456-7890", "123-456-7890", "123.456.7890"]
credit_cards = ["1234 5678 9012 3456", "1234-5678-9012-3456"]

for email in emails:
    print(email, (email))

for url in urls:
    print(url, (url))

for phone in phones:
    print(phone, (phone))

for card in credit_cards:
    print(card, (card))
