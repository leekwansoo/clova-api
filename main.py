import requests
import uuid
import time
import base64
import json

api_url = 'https://6se9xky39p.apigw.ntruss.com/custom/v1/28315/84f1980ab8751660f844a7e6838b1324314b4aea330aa75ad7de0c62a1e807b3/general'
secret_key = 'QkVaU1hOTU5EZGJXd0hQVXhMeExtQkFJeXBDSVhsVkU='
#image_url = 'https://1drv.ms/i/s!Ao7Rpx47gw4wir0ZEdbiJjI47Dxryw?e=mWKNVW'
image_file = 'page0.png'
with open(image_file,'rb') as f:
    file_data = f.read()

request_json = {
    'images': [
        {
            'format': 'png',
            'name': 'demo',
            'data': base64.b64encode(file_data).decode()
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = json.dumps(request_json).encode('UTF-8')
headers = {
  'X-OCR-SECRET': secret_key,
  'Content-Type': 'application/json'
}

response = requests.request("POST", api_url, headers=headers, data = payload)

result = json.loads(response)
print(result["images"])