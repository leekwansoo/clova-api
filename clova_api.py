import requests
import uuid
import time
import json

api_url = 'https://6se9xky39p.apigw.ntruss.com/custom/v1/28315/84f1980ab8751660f844a7e6838b1324314b4aea330aa75ad7de0c62a1e807b3/general'
secret_key = 'QkVaU1hOTU5EZGJXd0hQVXhMeExtQkFJeXBDSVhsVkU='
image_file = 'page0.png'

request_json = {
    'images': [
        {
            'format': 'png',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)
print(response)
print(response.text.encode('utf8'))