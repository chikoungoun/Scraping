
import smtplib


""" confirmation par mails """
def confirmation_mail(scrape_file):
    t = datetime.now()
    day = str(t.day) +"/"+str(t.month)+"/"+str(t.year)
    hour = str(t.hour)+":"+str(t.minute)+":"+str(t.second)
    temps = str(day)+"    "+str(hour)

    EMAIL_ADDRESS = 'gharwissen@gmail.com'
    EMAIL_PASSWORD = 'xxxxxx'


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        subject = str(scrape_file) + " du "+str(temps)
        body = "Mail de confirmation d'export réussi pour : "+ str(scrape_file)

        msg = (f'Subject:{subject}\n\n{body}').encode('utf-8')

        smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)

""" Update  Github """
#Connect to Github Repo
from github import Github

from datetime import datetime
import json

print("###########    Exporter  ################# \n \n")

"""  Reading the JSON File   """
file_path = "C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/PDG_Phone/neo_pdg.json"
with open(file_path) as json_file:
    data = json.load(json_file)

print(data)

""" Updating the Github link """
g = Github('4440d63ed3b2fe00c1c3803deae5e5006cd89eda')
print(g.get_user())

repo = g.get_user().get_repo('PDG')
print(repo)

file = repo.get_contents('casa_pdg.json')

repo.update_file('casa_pdg.json',str(datetime.now()),str(data),file.sha)

print('File updated')


confirmation_mail('Pharmacie de garde')
print('Mail envoyé')
