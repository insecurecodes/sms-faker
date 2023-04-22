# SMS Faker
This is a Python script that sends text messages to multiple phone numbers using the Textbelt API. The phone numbers and message are read from external files, and a random user agent is used for each request.

Textbelt has a limit of 1 request per number, this may change in the future and can cause the script to stop working.

## Usage
Clone the repository:

```bash
git clone https://github.com/insecurecodes/sms-faker.git
```

Install the required packages:


```bash
pip3 install -r requirements.txt
```

Create a file named `message.txt` in the same directory as the script and add the message you want to send.

Create a file named `phones.txt` in the same directory as the script and add the phone numbers you want to send the message to, one number per line.

Run the script:

```
python3 sms-faker.py
```
The script will send the message to each phone number in the phone.txt file using a random user agent for each request.

## Credits
This script uses the following libraries:

[requests](https://pypi.org/project/requests/) for making HTTP requests.

[fake_useragent](https://pypi.org/project/fake-useragent/) for generating random user agents.
