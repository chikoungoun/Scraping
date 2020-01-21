
# coding: utf-8

import os
import mylib.constantes as CONST
path = CONST.const

from mylib.mailing import confirmation_mail

# ## Immaculate perfect thanks

# In[1]:
""" ACCESS THE NEEDED WEBSITE """

import json
import requests

search_term = '1000 bruxelles'

url1 = 'https://api.tomtom.com/search/2/geocode/{}.json?key=ixTHgmn1oIBAMGhFbkAWgG5ajGKI4psb&limit=1&countrySet=BE'
url2 = 'https://api.geowacht.be/api-v4/json/pharmacies/near_coordinate?&latitude={}&longitude={}&jsonp=?&max_distance=30&max_results=5&language=fr'

data = requests.get(url1.format(search_term)).json()

lat, lon = data['results'][0]['position']['lat'], data['results'][0]['position']['lon']

data = requests.get(url2.format(lat, lon), headers={'Api-user-agent':'gwapi.js/4.0 (pharmacie.be)'}).json()

# print(json.dumps(data, indent=4)) # <-- uncomment to see all data

pharmacies = []
adresses = []
cps = []
coors = []
phones = []


""" Run through the data and extract what is needed """

for result in data['results']:
    print(result['pharmacy']['name'])
    pharmacies.append(result['pharmacy']['name'])

    print(result['pharmacy']['address_street'], result['pharmacy']['address_streetnr'])
    adresses.append(str(result['pharmacy']['address_streetnr'])+", "+result['pharmacy']['address_street'])

    print(result['pharmacy']['address_postalcode'], result['pharmacy']['address_locality'])
    cps.append(str(result['pharmacy']['address_postalcode'])+" "+result['pharmacy']['address_locality'])

    print(result['pharmacy']['coordinate']['coordinates'])
    coors.append(str(result['pharmacy']['coordinate']['coordinates'][0])+","+str(result['pharmacy']['coordinate']['coordinates'][1]))

    print(result['pharmacy']['phone_nr_digits'])
    phones.append(result['pharmacy']['phone_nr_digits'])

    print('-' * 80)


combo = []
for i,j,k,l,m in zip(pharmacies,adresses,cps,coors,phones):

    t = (i,j,k,l,m)
    combo.append(t)


# ## convert into a pandas object
import pandas as pd

df = pd.DataFrame(combo,columns=['pharmacie','adresse','cp','coordonnee','telephone'])


# ## convert into a json file
df.to_json(path+"/bxl_pdg.json",orient="records")

#
confirmation_mail("BXL Scraping")

# envoi vers Exporter
print("Activer Exporter")
os.startfile(path+"/B_Exporter.py")




print("Done")
