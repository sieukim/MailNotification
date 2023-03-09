import requests
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
dynamo_url = os.environ['dynamo_url']

# PUT: {id: 운송장 번호, user: 사용자 이메일}
def put_item(id, user, dynamo_url=dynamo_url):
    requests.post(dynamo_url+f'?id={id}&user={user}')

