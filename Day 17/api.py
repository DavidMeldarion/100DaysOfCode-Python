import requests
import base64
import json

response = requests.get("https://opentdb.com/api.php?amount=50&type=boolean&encode=base64").json()
data=[]
temp=response["results"]

for item in temp:
    temp_dict={}
    for key,value in item.items():
        iteration=0
        if isinstance(value, list):
            for i in value:
                decoded_64_value = base64.b64decode(i)
                decoded_value = decoded_64_value.decode()
                temp_dict[key]=decoded_value
        else:
            decoded_64_value = base64.urlsafe_b64decode(value)
            decoded_value = decoded_64_value.decode()
            temp_dict[key]=decoded_value
    data.append(temp_dict)
question_data=data
# print(question_data)
