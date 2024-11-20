import requests
import json


def getProducts():
    api_product = 'https://dummyjson.com/products'
    response = requests.get(api_product)
    # print(dir(response))
    data = response.json()

    for producto in data["products"]:
        print(producto["id"])
        print(producto["title"])
        print(producto["price"])
        print("------------------")
        print("------------------")




def loginUser():
    api_user = 'https://dummyjson.com/auth/login'

    body = {
        "username": 'emilys',
        "password": 'emilyspass',
    }

    response = requests.post(api_user, json=body)

    return response



data = loginUser()
data.json()["accessToken"]