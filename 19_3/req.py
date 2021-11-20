import json
import requests

# Тип запроса GET
# res = requests.get(url, headers=headers, params=params)
# Тип запроса POST
# res = requests.post(url, headers=headers, data=data)
# Тип запроса DELETE
# res = requests.delete(url, **kwargs)
# Тип запроса PUT
# res = requests.put(url, data=data)


def get_api_key(email: str, passwd: str):
    headers = {
        'email': email,
        'password': passwd,
    }
    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
    status = res.status_code

    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result


print(get_api_key('kluck1812@gmail.com', 'klicKKluck1812'))
