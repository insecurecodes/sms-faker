#!/usr/bin/env python3

import requests
from fake_useragent import UserAgent

# Open message.txt and read the message
with open('message.txt', 'r') as f:
    message = f.read().strip()

# Open phone.txt and read the phone numbers
with open('phones.txt', 'r') as f:
    phone_numbers = [line.strip() for line in f]

# Create a UserAgent object
ua = UserAgent()

for phone in phone_numbers:
    # Set a random user agent for each iteration
    headers = {'User-Agent': ua.random}

    # Send the message to each phone number
    resp = requests.post('https://textbelt.com/text', {
        'phone': phone,
        'message': message,
        'key': 'textbelt',
    }, headers=headers)

    print(f"Response for {phone}: {resp.json()}")
