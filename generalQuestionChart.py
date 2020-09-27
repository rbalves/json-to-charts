import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import os


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

psdf = pd.DataFrame.from_dict(pesquisa)
labels = psdf['id']
sim = []
nao = []
as_vezes = []

for pergunta in pesquisa:
    pdf = pd.DataFrame.from_dict(pergunta)
    pdict = pdf['respostas'].value_counts().to_dict()
    sim.append(pdict['SIM'])
    nao.append(pdict['NAO'])
    as_vezes.append(pdict['AS VEZES'])

barWidth = 0.25

r1 = np.arange(len(sim))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.bar(r1, sim, color='#F44336', width=barWidth, edgecolor='white', label='Sim')
plt.bar(r2, nao, color='#4CAF50', width=barWidth, edgecolor='white', label='Não')
plt.bar(r3, as_vezes, color='#FFEB3B', width=barWidth, edgecolor='white', label='Às vezes')

plt.title('Respostas QAF')
plt.xticks([r + barWidth for r in range(len(sim))], labels)
plt.legend()

FILE_FOLDER = 'temp/img/'

if not os.path.isdir(FILE_FOLDER):
    os.mkdir(FILE_FOLDER)

plt.savefig(FILE_FOLDER + 'general-question-chart.png')
