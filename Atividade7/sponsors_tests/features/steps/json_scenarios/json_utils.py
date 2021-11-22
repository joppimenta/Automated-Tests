import requests
import json

def get_url():
    return 'https://test.jasgme.com/sgme/api'

def get_credentials():
    return {'login': 'joao.pimenta@dellead.com', 'password': 'abcd1234'}

def get_token():
    url = get_url()
    credentials_body = get_credentials()

    response = requests.post(f'{url}/authenticate/login', json=credentials_body)
    assert response.status_code == 200

    json_data = json.loads(response.text)

    token = json_data['token']

    auth = f'Bearer {token}'

    return auth