import requests
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
dynamo_url = os.environ['dynamo_url']

# DELETE: {id: 운송장 번호, user: 사용자 이메일}
def delete_item(id, dynamo_url=dynamo_url):
    requests.delete(dynamo_url+f'?id={id}')