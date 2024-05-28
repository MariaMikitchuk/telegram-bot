import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Environment variables are not loaded because there is no .env file')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_API_HOST = os.getenv('RAPID_API_HOST')
DEFAULT_COMMANDS = (
    ('start', 'Start the bot'),
    ('help', 'Print the help'),
    ('low', 'Request with a minimum parameter'),
    ('high', 'Request with a maximum parameter'),
    ('history', 'Output of the last 10 user commands'),
    ('cancel', 'Cancel the current operation'),
)
