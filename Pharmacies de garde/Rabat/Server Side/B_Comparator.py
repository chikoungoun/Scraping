import pickle
import pandas as pd


import numpy as np
def levenshtein(s, t, ratio_calc = False):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return "The strings are {} edits away".format(distance[row][col])

""" ------------------- ------------------------------ ---------------------------- """
#Load the full list
df = pd.read_csv("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/pdg_rabat.csv",delimiter=';',index_col=0)



#load the on duty list
duty = pickle.load(open("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/rabat_pdg.pickle",'rb'))
#print(duty)


print("############################ \n \n")

#list to store all the concerned rows
leventab = []

adresses = []
telephones = []
quartiers = []
# All this script loops through both tables to find correnspondance
for i, row_i in duty.iterrows():
    #temporary variable to get the highest levenshtein ratio
    high = 0

    for j,row_j in df.iterrows():
        #print(levenshtein(row_j['pharmacie'].lower(),row_i['nom'].lower(),ratio_calc=True))
        ratio = levenshtein(row_j['pharmacie'].lower(),row_i['nom'].lower(),ratio_calc=True)
        if ratio > high:
            high = ratio
            lev = row_j['pharmacie']

    print(" Lev : "+str(lev)+", High : "+str(high))
    #print(df.loc[df['pharmacie'] == lev])
    leventab.append(df.loc[df['pharmacie'] == lev])

    # Get the data from Duty
    adresses.append(row_i['adresse'])
    # telephones.append(row_i['telephone'])
    # quartiers.append(row_i['quartier'])
print(" *** Loop Done *** ")

# Concatenate the results and end up with a final pandas Dataframe with resetted indexes
print(leventab)
neo_df = pd.concat(leventab)
neo_df.reset_index(drop=True,inplace=True)

# Adding the extra data from the on duty pharmacies
neo_df['adresse'] = adresses
# neo_df['quartier'] = quartiers
# neo_df['telephone'] = telephones


#Sort data following Neighborhoods
# neo_df.sort_values(by='quartier',inplace=True)


print(neo_df)


""" Export the csv file result """

neo_df.to_csv("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/neo_pdg_rabat.csv",sep=";",header=True,encoding='utf-8')

""" Export the json file result """
neo_df.to_json("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/neo_pdg_rabat.json",orient="records")


print(" Exported !!! ")
