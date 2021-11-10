#!/usr/bin/env python
# coding: utf-8


## Import Libraries
import pandas as pd
import streamlit as st
import urllib.request
import json

filmes = pd.read_csv("movies.csv")
# classes_filmes = pd.read_csv("filmes-Final.csv")
classes_filmes = pd.read_csv("processed_movies_2.csv")

# título
st.title("Web Movies Recomendation") 
# subtítulo
st.markdown("equipe: Adiel Silva - awbds.cid20@uea.edu.br ")
st.markdown(" Felipe Brasil - fbg.cid20@uea.edu.br")
st.markdown("Franklin Perseu - fpdll.cid20@uea.edu.br")
st.markdown("William dos Santos - wdsa.cid20@uea.edu.br")
# subtítulo
st.markdown("Trabalho de apresentação para o módulo:")
st.markdown("Infraestrutura em Nuvem para Projetos com Ciência dos Dados")


# st.markdown("Coloque um número randomico")
# filmeId = st.text_input("filme Id", key="filmeId", value=0)
st.markdown("Selecione as categorias Desejadas:")
# Adventure = st.text_input("Adventure", key="Adventure", value=0)
Adventure = st.checkbox("Adventure")
if Adventure:
    Adventure = 1
else:
     Adventure = 0
# Animation = st.text_input("Animation", key="Animation", value=0)
Animation = st.checkbox("Animation")
if Animation:
    Animation = 1
else:
    Animation = 0
# Action = st.text_input("Action", key="Action", value=0)
Action = st.checkbox("Action")
if Action:
    Action = 1
else:
    Action = 0
# Comedy = st.text_input("Comedy", key="Comedy", value=0)
Comedy = st.checkbox("Comedy")
if Comedy:
    Comedy = 1
else:
    Comedy = 0
# Crime = st.text_input("Crime", key="Crime", value=0)
Crime = st.checkbox("Crime")
if Crime:
    Crime = 1
else:
    Crime = 0
# Children = st.text_input("Children", key="Children", value=0)
Children = st.checkbox("Children")
if Children:
    Children = 1
else:
    Children = 0
# Drama = st.text_input("Drama", key="Drama", value=0)
Drama = st.checkbox("Drama")
if Drama:
    Drama = 1
else:
    Drama = 0
# Documentary = st.text_input("Documentary", key="Documentary", value=0)
Documentary = st.checkbox("Documentary")
if Documentary:
    Documentary = 1
else:
    Documentary = 0
# FilmNoir = st.text_input("Film-Noir", key="FilmNoir", value=0)
FilmNoir = st.checkbox("FilmNoir")
if FilmNoir:
    FilmNoir = 1
else:
    FilmNoir = 0
# Fantasy = st.text_input("Fantasy", key="Fantasy", value=0)
Fantasy = st.checkbox("Fantasy")
if Fantasy:
    Fantasy = 1
else:
    Fantasy = 0
# Horror = st.text_input("Horror", key="Horror", value=0)
Horror = st.checkbox("Horror")
if Horror:
    Horror = 1
else:
    Horror = 0
# IMAX = st.text_input("IMAX", key="IMAX", value=0)
IMAX = st.checkbox("IMAX")
if IMAX:
    IMAX = 1
else:
    IMAX = 0
# Romance = st.text_input("Romance", key="Romance", value=0)
Romance = st.checkbox("Romance")
if Romance:
    Romance = 1
else:
    Romance = 0
# SciFi = st.text_input("Sci-Fi", key="SciFi", value=0)
SciFi = st.checkbox("SciFi")
if SciFi:
    SciFi = 1
else:
    SciFi = 0
# Thriller = st.text_input("Thriller", key="Thriller", value=0)
Thriller = st.checkbox("Thriller")
if Thriller:
    Thriller = 1
else:
    Thriller = 0
# Musical = st.text_input("Musical", key="Musical", value=0)
Musical = st.checkbox("Musical")
if Musical:
    Musical = 1
else: 
    Musical = 0
# Mystery = st.text_input("Mystery", key="Mystery", value=0)
Mystery = st.checkbox("Mystery")
if Mystery:
    Mystery = 1
else:
    Mystery = 0 
# War = st.text_input("War", key="War", value=0)
War = st.checkbox("War")
if War:
    War = 1
else:
    War = 0
# Western = st.text_input("Western", key="Western", value=0)
Western = st.checkbox("Western")
if Western:
    Western = 1
else:
    Western = 0




# inserindo um botão na tela
btn_predict = st.button("Recomendar Filmes!")

if btn_predict:
    data = {
        "Inputs": {
                "input1":
                [
                    {
                        
                        'filmeId': "1",   
                        'nota_media': "1",  
                        'Horror': Horror,   
                        'Crime': Crime,   
                        'Children': Children,   
                        'Thriller': Thriller,   
                        'Film-Noir': FilmNoir,   
                        'Documentary': Documentary,   
                        'Fantasy': Fantasy,   
                        'Mystery': Mystery,   
                        'Comedy': Comedy,   
                        'Drama': Drama,   
                        'Musical': Musical,   
                        'Adventure': Adventure,   
                        'Romance': Romance,   
                        'War': War,   
                        'Animation': Animation,   
                        'IMAX': IMAX,   
                        'Action': Action,   
                        'Western': Western,   
                        'Sci-Fi': SciFi,   
                        'class': "0",     

                    }
                ],
        },
        "GlobalParameters":  {
     }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/88cee1267b3f4781be5764f390ed1fa2/services/a8a394e8054047aa97b3e932b21caa95/execute?api-version=2.0&format=swagger'
    api_key = 'CCirVzTtQj3meO/D1MdYxlKdzaYTNoPtm9hJRrb8CNG7fCOEHDczlGfakhxQ/76dRzz6G5iB4zgEQtnWQlyEtg==' 

    # url = 'https://ussouthcentral.services.azureml.net/workspaces/88cee1267b3f4781be5764f390ed1fa2/services/f1e5d50315564cc3ab193edfeea56489/execute?api-version=2.0&format=swagger'
    # api_key = '6WkC96kzPJulU1jWjo76ZqZUVmBKiqrB6Adk7rROj/EKvEVVkfu3z45A/iSPpayY7aUM1T5bgr4NgPkzov5N6Q==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result )
        parsed_json = (json.loads(result))

        print(parsed_json)
        y = json.loads(json.dumps(parsed_json, indent=4, sort_keys=True))
        x = y['Results']
        z = x['output1']
        m = z[0]

        # st.markdown(z)

        label_retorno = int(m['Scored Labels'])
        classes_filmes =  classes_filmes[classes_filmes["class"] == label_retorno]      
        classes_filmes = classes_filmes.sample(n=5)
        for i in range(5):
            st.markdown(filmes["title"][filmes["movieId"] == classes_filmes.iloc[i,0]].values)
            
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
else:
    print("error")
    
	
	
