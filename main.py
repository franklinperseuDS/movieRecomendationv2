# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, request, jsonify
import pickle

#criar app
app = Flask(__name__)

#movies
movies = pd.read_csv("movies.csv")
#coluna de dados
colunas = ['filmeId', 'nota_media', 'Drama', 'Documentary', 'Romance', 'Action',
       'Adventure', 'IMAX', 'Horror', 'War', 'Musical', 'Sci-Fi', 'Fantasy',
       'Animation', 'Film-Noir', 'Crime', 'Mystery', 'Children', 'Comedy',
       'Western', 'Thriller']

#colunas = ['id','filmeId']


def load_model( file_name = 'decision_tree.pkl'):
    return pickle.load(open(file_name, "rb"))

modelo = load_model('decision_tree.pkl')

@app.route('/reco/<id>')
def show_id(id):
    return f'Recebendo dados \n ID: {id}'

@app.route('/reco/', methods=['POST'])
def get_recomendations():
   
    dados = request.get_json()
    playload = np.array([dados[col] for col in colunas])
    
    playload = playload.reshape(1, -1)
    score = np.float(modelo.predict(playload))
    score = int(score)
    if(score):
        return f'O filme que recomendamos para você é {movies.iloc[score][1]}'

    else:
        return 'nada aqui'
    
    

@app.route('/')
def home():
    return 'API de predição de filmes'

app.run(debug=True)



