
from dotenv import load_dotenv
import os


load_dotenv()

PROJECT=os.getenv('PROJECT')
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
AUTH_MODE=os.getenv('AUTH_MODE', 'password')
OUTPUT_FORMAT=os.getenv('OUTPUT_FORMAT', 'markdown')
OUTPUT=os.getenv('OUTPUT', '')
