import pandas as pd

import urllib.request
import json

filmes = pd.read_csv("movies.csv")
classes_filmes = pd.read_csv("filmes-Final.csv")

# print(classess.info())

label_retorno = 7
classes_filmes =  classes_filmes[classes_filmes["class"] == label_retorno]      
# classes_filmes = classes_filmes[classes_filmes["nota_media"] > 3]
classes_filmes = classes_filmes.sample(n=5)
print(classes_filmes.head())
for i in range(5):
    print(filmes["title"][filmes["movieId"] == classes_filmes.iloc[i,1]].values)

#6316          4876          5785         5784  7764                   