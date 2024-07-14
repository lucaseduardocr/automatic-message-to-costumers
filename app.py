import pandas as pd
import pyautogui
import tkinter
import webbrowser
import datetime
from time import sleep
from urllib.parse import quote


data_atual = datetime.date.today()
data_atual_formatada = data_atual.strftime("%d/%m/%Y")

webbrowser.open('https://web.whatsapp.com/')
sleep(30)

caminho_absoluto = r'C:\Users\lucas\Projetos\euvendedor\aniversarioclienteschevrolet.xlsx'

planilha = pd.read_excel(caminho_absoluto)

for indice, linha in planilha.iterrows():
    nome = linha[0]
    numero_telefone = [1]
    data_aniversario = linha[2]

mensagem = f"Olá {nome}, aqui é o Lucas da Jorlan, tudo bem ? Reparei aqui que hoje é seu aniversário! Entrando em contato para desejar felicidades! Que hoje, dia {data_aniversario.strftime('%d/%m/%Y')} seja memorável na sua vida! Parabéns!"

link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={numero_telefone}&text={quote(mensagem)}'
webbrowser.open(link_mensagem_whatsapp)
input('')