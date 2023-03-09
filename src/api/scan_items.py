import requests
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
dynamo_url = os.environ['dynamo_url']

# SCAN: {id: 운송장 번호, user: 사용자 이메일} 리스트 
def scan_items(dynamo_url=dynamo_url):
    response = requests.get(dynamo_url).json()
    items = response['Items']
    return items