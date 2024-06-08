import requests
from datetime import datetime

USERNAME="anuj0812"
TOKEN="dvhbvhbkdbvkbsdkvhsdbv"
GRAPH_ID="graph12"


pixela_endpoint="https://pixe.la/v1/users"


user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)


graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":"graph12",
    "name":"Daily Check graph",
    "unit":"commit",
    "type":"int",
    "color":"sora"
}
headers={
    "X-USER-TOKEN":TOKEN,
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.now()

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many daily work done today?"),

}

headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(response.text)


pixel_update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


new_pixel_data={
    "quantity":"552",
}

headers={
    "X-USER-TOKEN":TOKEN
}

# response=requests.put(url=pixel_update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)
 

pixel_delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}" 
 
response=requests.delete(url=pixel_delete_endpoint,headers=headers)
print(response.text )