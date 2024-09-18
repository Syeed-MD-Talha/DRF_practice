import requests  
data=requests.get(url='http://127.0.0.1:8000/aiquest_info/')
data=data.json()
print(data)




# import  requests  

# URL='http://127.0.0.1:8000/aiquest_info/'

# response=requests.get(url=URL)
# data=response.json()
# print(data)
