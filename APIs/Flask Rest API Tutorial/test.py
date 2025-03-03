import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "video/0")
#>>>SEND in postman after selecting request type(GET)

# response = requests.put(BASE + "video/2",{})
#>>>Enter the data for new entry in JSON format inside body/raw in postman after selecting request type(PUT)

# response = requests.patch(BASE + "video/2", {"views":999, "likes":1222})
#>>>Enter the data to be edited in JSON format inside body/raw in postman after selecting request type(PATCH)

response = requests.delete(BASE + "video/2")
#>>>SEND in postman after selecting request type(DEL)


print(response.json())

