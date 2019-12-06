
# coding: utf-8
import datetime
from datetime import datetime

""" Pharmacie de garde de Nuit """

# **Fonction extraction téléphone**
def telephone_pharmacie(adress):
    #renverser la chaine de caractères
    adress[::-1]

    #extraire le téléphone inversé
    ntel = ''
    for i in adress[::-1]:
        if i == ':':
            break
        elif i.isnumeric():#uniquement ajouter les nombres
            ntel = ntel + i
        else:
            continue

    #remettre le num de tel à l'endroit
    tel = ''
    for i in ntel[::-1]:
        tel = tel + i

    return tel.strip()


# **Fonction effacer téléphone** ( renvoie l'adresse seule
def effacer_telephone(d):
    #renverser la chaîne
    nd = d[::-1]
    #trouver la position du dernier tiret
    c = nd.find('-')
    #retourner la sous chaine de caractère depuis la position+1
    snd = nd[(c+1):].strip()
    #inverser la sous chaîne une deuxième fois
    pnd = snd[::-1]

    return pnd



# # Scraping des pharmacies de garde sur Casablanca
# source des données : https://lematin.ma/pharmacie-garde-casablanca.html
import requests

url = 'https://lematin.ma/pharmacie-garde-casablanca/nuit.html'
response = requests.get(url)
response

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text,'html.parser')
type(soup)


quartiers = soup.find_all('div',class_='lespharmaciengarde')

# **Liste des liens des quartiers **
liens = []
for i in quartiers:
    liens.append("https://lematin.ma"+str(i.find('a')['href']))

for i in liens:
    print(i)


# ** Liste des quartiers **
liste_quartiers = []
for i in quartiers:
    liste_quartiers.append(i.find('h4').text)
    print(i.find('h4').text)



# Scrap page par page
from time import time
from time import sleep
from random import randint

start_time = time()
requests = 0

from requests import get

noms =[]
adresses = []
quartiers = []
telephones = []

for i,j in zip(liens,liste_quartiers):
    print(i)
    response = get(i)

    timer = randint(8,15)
    #pause de loop
    print(timer)
    sleep(timer)

    #renvoyer un warning pour les non 'status code : 200'
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

    #parser en BS
    page_html = BeautifulSoup(response.text,'html.parser')

    pharmacies = page_html.find_all('div',class_='pharmacie')

    """ Noms et adresse """
    for k in pharmacies:
        noms.append(k.find('h5').text)
        adresses.append(effacer_telephone(k.find('p').text))
        quartiers.append(j)
        telephones.append(telephone_pharmacie(k.find('p').text))





print('*** *** Done *** ***')

garde = []
for i,j,k,l in zip(noms,adresses,quartiers,telephones):
    t = (i,j,k,l)
    garde.append(t)

print(garde)


# ## Convertir en objet pandas
import pandas as pd
df = pd.DataFrame(garde,columns=['nom','adresse','quartier','telephone'])




# ### Serializer la liste et l'exporter en fichier binaire
import pickle


pickle_out = open("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/pdg.pickle","wb")
pickle.dump(df,pickle_out)
pickle_out.close()

print("PDG pickled")
