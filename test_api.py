import requests


headers = {
        "x-api-key": "free_user_3FbOjeQMrryYeXOOfBOPFm3L3A3" 
    }

def test_create_user():
    url = "https://reqres.in/api/users" 
    
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    
    # 2. Передаем headers в запрос как отдельный аргумент
    response = requests.post(url, json=payload, headers=headers)
    
    assert response.status_code == 201
    
    response_data = response.json()
    assert response_data["name"] == "morpheus"

def test_update_user():
    url = "https://reqres.in/api/users/2"

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(url, json=payload, headers=headers)

    assert response.status_code == 200


def test_delete_user():
    url = "https://reqres.in/api/users/2"

    response = requests.delete(url, headers=headers)

    assert response.status_code == 204