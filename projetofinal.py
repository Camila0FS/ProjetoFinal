# Programa 4 - Projeto Final
# Descrição:
# Este programa organiza os arquivos nas pastas planilhas e documentos.

# Autor: Camila Freitas Sant Ana
# Versão: 0.0.1 # Data: 14/09/2022

# Anotações: gravar na memória dados abertos - balancete - do do TCE-RS

# Abrir terminal - via jupiter notebook
# C:\Users\Users> cd projeto1
# C:\Users\Users> ls (listou os arquivos)
# C:\Users\Users> mkdir projetofinal
# C:\Users\Users\ cd projetofinal
# C:\Users\Users\projetofinal> 

# No jupiter notebook new ipykernel - renomeado projetofinal.py

# Importando requests


import requests

# Lendo a página dos Dados Abertos do TCE-RS
endereco = "http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv"

dados = requests.get(endereco)
dados.status_code

type(dados)

# Gravando o qrquivo com as informações da variável pagina

balancete = open('balancete.csv', 'wb')
for texto in dados.iter_content(1048576):
        balancete.write(texto)
balancete.close()

# importando pacote openpyxl e definando variável

from openpyxl import Workbook
wb = Workbook("balancete.csv")

# importando pacote pandas e definindo sigla para reconhecimento

import pandas as pd

# usando pandas para ler .CSV e demonstrar aquivo com a definição da variável balancete

balancete = pd.read_csv('balancete.csv')

balancete.head()

# usando pandas para ler .XlSX e demonstrar aquivo com a definição da variável novo_balancete

balancete.to_excel("balancete.xlsx")

novo_balancete = pd.read_excel('balancete.xlsx')

novo_balancete.head()

print(f"novo_balancete", "formato xlsx gerado com sucesso!")
