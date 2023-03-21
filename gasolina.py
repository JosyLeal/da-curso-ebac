# código de geração do gráfico - 
import seaborn as sns
import pandas as pd

data = pd.read_csv("gasolina.csv", sep=",")
data

from matplotlib.offsetbox import BboxImage
#Gerando o gráfico
from seaborn.relational import lineplot
with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data = data, x = "dia", y = "venda", palette="pastel")
  grafico.axes.set_title("Preço médio da gasolina em São Paulo/SP (01/06 a 10/06 de 2021",fontweight= 'bold')
  grafico.set_xlabel("Dia")
  grafico.set_ylabel("Preço médio")

  #Salvando a imagem em um arquivo pdf ou png
grafico.figure.savefig(fname = "gasolina.png",bbox="tight")