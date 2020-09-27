import pandas as pd
import requests
import matplotlib.pyplot as plt
import os


URL = 'https://jsonbox.io/box_9da5210c1a35783aa3a7'

response = requests.get(URL)
json = response.json()

df = pd.DataFrame.from_dict(json)

df['grau'].value_counts().sort_index().plot.bar(color=['#FF9800', '#FFEB3B', '#F44336', '#4CAF50'])

FILE_FOLDER = 'temp/img/'

if not os.path.isdir(FILE_FOLDER):
    os.mkdir(FILE_FOLDER)

plt.title('Grau de acometimento')
plt.subplots_adjust(bottom=0.25)
plt.xticks(rotation=45)
plt.savefig(FILE_FOLDER + 'grade-chart.png')
