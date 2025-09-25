import requests

#response= requests.get('https://www.instagram.com')

#print(response.status_code)
#print(response.text)
print("------z-----")

import requests

usuario={
    "name":"emrehliug",
}
#response=requests.post('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos',json=usuario)
response=requests.delete('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos/1',json=usuario)


print(response.status_code)
print(response.json())