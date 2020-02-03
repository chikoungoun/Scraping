
# coding: utf-8
import os
import mylib.constantes as CONST
path = CONST.const

from mylib.mailing import confirmation_mail


import requests


url = 'https://www.med.tn/pharmacie/garde/tunis'
response = requests.get(url)
response

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text,'html.parser')
type(soup)


results = soup.find('div',class_="resultsxyz")



# ### Neighborhood links
slider = results.find_all('a',class_="btn btn-default btn-sm")

liens_quartiers = []
for i in slider:
    print(i['href'])
    liens_quartiers.append(i['href'])


# ### Neighborhood names
noms_quartiers = []
for i in slider:
    print(i.text)
    noms_quartiers.append(i.text[:i.text.find('(')].strip())

# ### Neighborhood duo
duo_quartier = []
for i,j in zip(liens_quartiers,noms_quartiers):
    t = (i,j)
    duo_quartier.append(t)


for i in duo_quartier:
    print(i[1])


# ## Scraping link by link
from time import time
from time import sleep
from random import randint

start_time = time()
requests = 0


from requests import get

noms = []
pre_adresses = []
pre_coors = []
phones = []
quartiers = []

for i in duo_quartier:
    print(i[0])

    response = get(i[0])

    timer = randint(8,15)
    #pause de loop
    print(timer)
    sleep(timer)

    #Scraping the links
    soup = BeautifulSoup(response.text,'html.parser')

    results = soup.find_all('div',class_="searchResults-itemDoctor")

    for j in results:
        #Setting the neighborhood
        print(i[1])
        quartiers.append(i[1])


        # Scraping the names
        print(j.find('span',class_='practitioner-name').text)
        noms.append("Pharmacie "+(j.find('span',class_='practitioner-name').text).lower())

        # Scraping the adresses
        print((j.find('div',class_='practitioner-address').find('p').text).strip())
        pre_adresses.append((j.find('div',class_='practitioner-address').find('p').text).strip())

        # Scraping the phone numbers
        print(j.find('span',class_='view-tel').text)
        phones.append((j.find('span',class_='view-tel').text).replace('.',''))

        # Scraping the coordinates
        print(j.find('a',class_='btn').findNext('a')['href'])
        pre_coors.append(j.find('a',class_='btn').findNext('a')['href'])


print(" *** Done ***")


# ### cleaning up adresses
adresses = []
for i in pre_adresses:
    adresses.append(i.replace('Tunisie','').replace('  ','').lower())


# ### cleaning up coordinates
coors = []
for i in pre_coors:
    eq = i.find('=')
    print(i[eq+1:])
    coors.append(i[eq+1:])


for i,j in enumerate(coors):
    if "tel" in coors[i]:
        print('yep')
        coors[i] = "NO COORDINATES"

# ## Merging the data we got
garde = []
for i,j,k,l,m in zip(noms,quartiers,adresses,coors,phones):
    t = (i,j,k,l,m)
    garde.append(t)


# ### Convert into a Pandas Object
import pandas as pd

df = pd.DataFrame(garde,columns=['nom','quartier','adresse','coordonnee','telephone'])

# ### Sort the data by neighborhood name
df.sort_values(by='quartier',inplace=True)

df.reset_index(drop=True,inplace=True)




# ### Serialization
import pickle

pickle_out = open(path+"/Pickles/tunis_garde.pickle","wb")
pickle.dump(df,pickle_out)
pickle_out.close()
