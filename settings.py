
from dotenv import load_dotenv
import os


load_dotenv()

DET_FILE_DIRECTORY = os.getenv('DET_FILE_DIRECTORY', 'det_configs')

# commcare-export config
PROJECT=os.getenv('PROJECT')
USERNAME=os.getenv('USERNAME')
PASSWORD=os.getenv('PASSWORD')
AUTH_MODE=os.getenv('AUTH_MODE', 'password')
OUTPUT_FORMAT=os.getenv('OUTPUT_FORMAT', 'markdown')
OUTPUT=os.getenv('OUTPUT', '')
BATCH_SIZE=os.getenv('BATCH_SIZE', 100)
