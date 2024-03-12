import requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()

# display it in json format
print(data)

# number of people I retrieved then printed
number = data["number"]
print(number)

# people's names retieved and displayed
for person in data["people"]:
    print(person["name"])
