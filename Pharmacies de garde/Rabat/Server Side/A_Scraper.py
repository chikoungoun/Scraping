
# coding: utf-8

import os
import mylib.constantes as CONST
path = CONST.const

from mylib.mailing import confirmation_mail


""" *** Scrape depuis vie viepratique *** """

# # Scraping des pharmacies de garde sur Rabat
import requests

url = 'http://www.viepratique.ma/pharmacies-de-garde/rabat-Maroc'
response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text,'html.parser')
type(soup)

articles = soup.find_all('article',class_ = 'one_element')

print(articles[:100])
print(len(articles))


# ### Scraping the pharmacies names
noms = []
for i in articles:
    print(i.find('h2').text[1:])
    noms.append(i.find('h2').text[1:])

# ### Scraping the pharmacies adresses
adresses = []
for i in articles:
    print(i.find('div',class_='adress-container').text)
    adresses.append(i.find('div',class_='adress-container').text)


# ### Scraping the phone numbers
p = soup.find_all('div',class_='number_phone')


phones = []
for i in p:
    print(i.find_next_sibling().text)
    phones.append(i.find_next_sibling().text)


# ## Merge the data we got so far
garde = []
for i,j,k in zip(noms,adresses,phones):
    t = (i,j,k)
    garde.append(t)


# ## Convert into Pandas object
import pandas as pd

df = pd.DataFrame(garde,columns=['nom','adresse','telephone'])

print(df)

#export the file in csv
#df.to_csv(path+"/pdg_rabat.csv",sep=";",header=True,encoding='utf-8')


""" Export Pickle File """
import pickle

pickle_out = open(path+"/pdg_rabat.pickle","wb")
pickle.dump(df,pickle_out)
pickle_out.close()

import time
time.sleep(2 )

print("PDG pickled")
os.startfile(path+"/B_Phone_Comparator.py")
