# coding: utf-8

# # Scraping des pharmacies de garde sur Rabat
import requests

url = 'http://www.viepratique.ma/pharmacies-de-garde/rabat-Maroc'
response = requests.get(url)
response

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text,'html.parser')
type(soup)



articles = soup.find_all('article',class_ = 'one_element')



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


# ## Merge the data we got so far
garde = []
for i,j in zip(noms,adresses):
    t = (i,j)
    garde.append(t)

print(garde)

# ## Convert into Pandas object
import pandas as pd

df = pd.DataFrame(garde,columns=['nom','adresse'])

print(df)


# ### Serializer la liste et l'exporter en fichier binaire
import pickle


pickle_out = open("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/rabat_pdg.pickle","wb")
pickle.dump(df,pickle_out)
pickle_out.close()

print("PDG pickled")
