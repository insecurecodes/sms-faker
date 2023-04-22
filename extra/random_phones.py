import random

# List of country codes to choose from
country_codes = ['1', '44', '86', '91', '234', '353', '972', '977', '971', '998']

# Generate 10 random phone numbers with the format +<country code><10 digits>
phone_numbers = ['+' + random.choice(country_codes) + ''.join([str(random.randint(0, 9)) for _ in range(10)]) for _ in range(10)]

# Print the list of phone numbers without numbering
for phone in phone_numbers:
    print(phone)