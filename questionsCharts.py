import pandas as pd
import requests
import os
import matplotlib.pyplot as plt


pesquisa = [
    {
        'id': 'Q01',
        'descricao': 'Sente dificuldade para abrir a boca?',
        'respostas': []
    },
    {
        'id': 'Q02',
        'descricao': 'Você sente dificuldades para movimentar sua mandíbula para os lados?',
        'respostas': []
    },
    {
        'id': 'Q03',
        'descricao': 'Tem cansaço/dor muscular quando mastiga?',
        'respostas': []
    },
    {
        'id': 'Q04',
        'descricao': 'Sente dores de cabeça com frequência?',
        'respostas': []
    },
    {
        'id': 'Q05',
        'descricao': 'Sente dor na nuca ou torcicolo?',
        'respostas': []
    },
    {
        'id': 'Q06',
        'descricao': 'Tem dor de ouvido ou na região das articulações (ATMs)?',
        'respostas': []
    },
    {
        'id': 'Q07',
        'descricao': 'Já notou se tem ruídos na ATM quando mastiga ou quando abre a boca?',
        'respostas': []
    },
    {
        'id': 'Q08',
        'descricao': 'Você já observou se tem algum hábito como apertar e/ou ranger os dentes (mascar chiclete, morder o lápis ou lábios, roer a unha)?',
        'respostas':[]
    },
    {
        'id': 'Q09',
        'descricao': 'Sente que seus dentes não se articulam bem?',
        'respostas': []
    },
    {
        'id': 'Q10',
        'descricao': 'Você se considera uma pessoa tensa ou nervosa?',
        'respostas': []
    },
]

alternativas = {
    0: 'NAO',
    5: 'AS VEZES',
    10: 'SIM'
}

URL = 'https://jsonbox.io/box_9da5210c1a35783aa3a7'

response = requests.get(URL)
json = response.json()

df = pd.DataFrame.from_dict(json)

for indice_pergunta in range(len(pesquisa)):
    for resposta in df['respostas']:
        pesquisa[indice_pergunta]['respostas'].append(
            alternativas[resposta[indice_pergunta]]
        )

for pergunta in pesquisa:
    pdf = pd.DataFrame.from_dict(pergunta)
    pdf['respostas'].value_counts().sort_index().plot.bar(color=['#ffeb3b', '#4caf50', '#f44336'])

    FILE_FOLDER = 'temp/img/'

    if not os.path.isdir(FILE_FOLDER):
        os.mkdir(FILE_FOLDER)

    plt.title(pergunta['id'])
    plt.subplots_adjust(bottom=0.15)
    plt.xticks(rotation=45)
    plt.savefig(FILE_FOLDER + pergunta['id'] + '.png')

    plt.close()
