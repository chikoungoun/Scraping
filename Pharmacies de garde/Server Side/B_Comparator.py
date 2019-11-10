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
df = pd.read_csv("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/pdg_full.csv",delimiter=';',index_col=0)



#load the on duty list
duty = pickle.load(open("C:/Users/marwane/Documents/Projets Python/Pharmacie_de_Garde/Comparator091119/pdg.pickle",'rb'))
#print(duty)


print("############################ \n \n")

leventab = []

for i, row_i in duty.iterrows():
    #print("Index i : "+str(i))
    high = 0

    for j,row_j in df.iterrows():
        #print(levenshtein(row_j['pharmacie'].lower(),row_i['nom'].lower(),ratio_calc=True))
        ratio = levenshtein(row_j['pharmacie'].lower(),row_i['nom'].lower(),ratio_calc=True)
        if ratio > high:
            high = ratio
            lev = row_j['pharmacie']

    print(" Lev : "+str(lev)+", High : "+str(high))
    leventab.append(lev)
print(" *** Loop Done *** ")

print(leventab)







#
# print("############################ \n \n")
#
# for i, row_i in df.iterrows():
#     high = 0
#     for j,row_j in duty.iterrows():
#         print(levenshtein(row_i['pharmacie'].lower(),row_j['nom'].lower(),ratio_calc=True))
#         ratio = levenshtein(row_i['pharmacie'].lower(),row_j['nom'].lower(),ratio_calc=True)
#         if ratio > high:
#             high = ratio
#             lev = row_i['pharmacie']
#     print(" Lev : "+str(lev)+", High : "+str(high))
# print(" *** Loop Done *** ")
#
