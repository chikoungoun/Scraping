import pickle
import pandas as pd
import os

#Load the full list
#Converters to keep the starting "0" in the phone number
df = pd.read_csv("C:/Users/marwane/Documents/Projets Python/Pharma_Casa/pdg_casa_full.csv",delimiter=';',index_col=0,converters={'telephone': lambda x: str(x)})
print(df.head())
print("df telephone type : "+df['telephone'])

#load the on duty list
duty = pickle.load(open("C:/Users/marwane/Documents/Projets Python/Pharma_Casa/pdg.pickle",'rb'))
print(duty.head())
print("duty telephone type : "+duty['telephone'])

print("###########    Comparator  ################# \n \n")



#list to store all the concerned rows
ph = []
adresses = []
telephones = []
quartiers = []

c = 0
for i, row_i in duty.iterrows():

    for j,row_j in df.iterrows():


        if(row_i['telephone'] == row_j['telephone']):
            print("Yosha !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")
            c = c+1
            # Get the data from Duty
            ph.append(df.loc[df['telephone'] == row_i['telephone']])

            quartiers.append(row_i['quartier'])
        else:
            print('Lame')



print(ph)
neo_df = pd.concat(ph)
neo_df.reset_index(drop=True,inplace=True)
print(neo_df)

neo_df['quartier'] = quartiers

#Sort data following Neighborhoods
neo_df.sort_values(by='quartier',inplace=True)


print(neo_df)

neo_df = neo_df[['pharmacie','lien','quartier','adresse','coordonnee','telephone']]

print(neo_df)

print("\n *** *** Done *** *** \n")
print(c)
