import pandas as pd
import requests
from bs4 import BeautifulSoup

# cities we want to scrape:
cities = ["Agadir", "Casablanca", "Rabat", "Fes"]

# first start by creating a list of the attributes we wants

pharmacy_names = []
pharmacy_addresses = []
pharmacy_telephones = []

# then we loop through the cities and scrape the data

for city in cities:
    page_to_scrape = f"https://www.annuaire-gratuit.ma/pharmacie-garde-{city}.html"

    # send the request to that particular url
    response = requests.get(page_to_scrape)
    # print(page_to_scrape)
    # check the status code and handle errors
    if response.status_code == 200:
        print("Request was successful")
        # specify the parser html.parser
        soup = BeautifulSoup(response.text, "html.parser")

        # parse pharmacy names then append to the list
        pharmcy_name = soup.find_all("h3", itemprop="name")
        for ph_name in pharmcy_name:
            # print(ph_name.text)
            pharmacy_names.append(ph_name.text)

        # parse pharmacy addresses then append to the list
        pharmacy_addres = soup.find_all("p", itemprop="streetAddress")
        for ph_add in pharmacy_addres:
            # print(ph_add.text)
            pharmacy_addresses.append(ph_add.text)

        phoneNumbers = soup.find_all(style="font-weight: bold; color:#1e6dab")
        # print(phoneNumbers.text)

        # parse pharmacy phone numbers then append to the list
        for phoneNumber in phoneNumbers:
            # print(phoneNumber.text)
            pharmacy_telephones.append(phoneNumber.text)
            # print(pharmacy_telephones)

        # here we'll create the dataframe
        data_pharmacies = pd.DataFrame(
            {
                "Name": pharmacy_names,
                "Address": pharmacy_addresses,
                "Telephone": pharmacy_telephones,
            }
        )
        # pharmacy_data = pd.DataFrame(city)

        # here I'll export the  data as csv
        data_pharmacies.to_csv(f"{city}.csv", index=False)
        # print(response.text)
        pharmacy_names.__len__()
        # clear the lists
        pharmacy_names.clear()
        pharmacy_addresses.clear()
        pharmacy_telephones.clear()
    else:
        print("Request Failed, with status code", response.status_code)

# but this scraping is not 100% correct, we need to fix it
# since if we don't have data we'll run into an error, becuse we can't
# create a datafram if we don't have the same lines for each column
