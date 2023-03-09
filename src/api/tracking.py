import dotenv
import os
import requests
import xmltodict

dotenv.load_dotenv(dotenv.find_dotenv())
dynamo_url = os.environ['dynamo_url']
tracking_url = os.environ['tracking_url']
tracking_key = os.environ['tracking_key']

# GET: {id: 운송장 번호}
def tracking(id, tracking_url=tracking_url, tracking_key=tracking_key):
    response = requests.get(tracking_url+f'?serviceKey={tracking_key}&rgist={id}')
    response = xmltodict.parse(response.text)['response']
    success = response['header']['successYN'] == 'Y'
    return success
