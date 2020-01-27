import pickle
import pandas as pd
import os

import mylib.constantes as CONST
path = CONST.const

#Load the full list
#Converters to keep the starting "0" in the phone number

df = pd.read_excel(path+'/Pharmacies_rabat.xlsx')

df['telephone']= df['telephone'].astype(str)
for i, row in df.iterrows():
    row['telephone'] = "0"+str(row['telephone'])

print(df.head())

print("Traiter la base df ")

#load the on duty list
duty = pickle.load(open(path+"/pdg_rabat.pickle",'rb'))


print("###########    Comparator  ################# \n \n")



#list to store all the concerned rows
ph = []
dt = pd.DataFrame()
# Loop throught the data and make a comparison of their phone numbers as a unique identifier
c = 0
for i, row_i in duty.iterrows():

    print(str(row_i['telephone']))

    for j,row_j in df.iterrows():

        print(row_j['telephone'])

        if(row_i['telephone'] == row_j['telephone']):
            print("Yosha !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
            c = c+1
            # Get the data from Duty
            ph.append(row_j)


        else:
            print('Lame')


dt=pd.DataFrame(ph,columns=['pharmacie','lien','coordonnee','adresse','telephone','quartier'])
print(c)
#print(ph)
print(dt)



dt.reset_index(drop=True,inplace=True)
print(dt)


""" Export the json file result """
dt.to_json(path+"/rbt_pdg.json",orient="records")

print(" Compared !!! ")

print("Activer Exporter")

import time
time.sleep(5)


os.startfile(path+"/C_Exporter.py")
print("après activation Exporter")
