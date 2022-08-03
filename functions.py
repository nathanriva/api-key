import requests
from dotenv import load_dotenv
import os
load_dotenv() 

response = requests.get('http://127.0.0.1:8000/private', auth=('user@example.com', format(os.getenv('atlassian_api_token'))))

print(response)