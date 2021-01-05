import requests
import json

url = "http://127.0.0.1:8000/client/88bvchvnsj7/collision"
ip_adress_params = {"ip_adress": "kaFKX"}
verify_backend_func = requests.post(url, params=ip_adress_params)
print(verify_backend_func.json())

"""

url = "http://127.0.0.1:8000/client/88bvchvnsj7/users"
#ip_adress_params = {"ip_adress": "89.90.145.202"}
verify_backend_func = requests.get(url)
print(verify_backend_func.json())
"""
