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
file_path = path+"/bxl_pdg.json"
with open(file_path) as json_file:
    data = json.load(json_file)

print(data)

""" Updating the Github link """
g = Github('6514108b63db6731f0478fc399cd6d6128c02c4a')
print(g.get_user())

repo = g.get_user().get_repo('PDG')
print(repo)

file = repo.get_contents('bxl_pdg.json')

repo.update_file('bxl_pdg.json',str(datetime.now()),str(data),file.sha)

print('File updated')


#confirmation_mail('Pharmacie de garde')
print('Mail envoyé')
