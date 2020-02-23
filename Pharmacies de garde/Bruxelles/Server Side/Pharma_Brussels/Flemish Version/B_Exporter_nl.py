import mylib.constantes as CONST
path = CONST.const

import smtplib


""" Update  Github """
#Connect to Github Repo
from github import Github

from datetime import datetime
import json

print("###########    Exporter  ################# \n \n")

"""  Reading the JSON File   """
file_path = path+"/bxl_pdg_nl.json"
with open(file_path) as json_file:
    data = json.load(json_file)

print(data)

""" Updating the Github link """
with open('api_git.txt') as f:
    api_key = f.readline()
    f.close

g = Github(api_key)

print(g.get_user())

repo = g.get_user().get_repo('PDG')
print(repo)

file = repo.get_contents('bxl_pdg_nl.json')

repo.update_file('bxl_pdg_nl.json',str(datetime.now()),str(data),file.sha)

print('File updated')


#confirmation_mail('Pharmacie de garde')
print('Mail envoyé')
