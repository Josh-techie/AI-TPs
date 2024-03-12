import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()

number = data["number"]
# number of people I retrieved
print(number)
# people's names retieved and displayed
for person in data["people"]:
    print(person["name"])
