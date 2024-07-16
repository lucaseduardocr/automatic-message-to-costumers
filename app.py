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
sleep(10)

caminho_absoluto = r'C:\Users\lucas\Projetos\euvendedor\aniversarioclienteschevrolet.xlsx'

planilha = pd.read_excel(caminho_absoluto)

for indice, linha in planilha.iterrows():
    nome = linha[0]
    numero_telefone = linha[1]
    data_aniversario = linha[2]
    print (numero_telefone)
    print(nome)
    print(data_aniversario)
    mensagem = f"Olá {nome}, aqui é o Lucas da Jorlan, tudo bem ? Reparei aqui que hoje é seu aniversário! Entrando em contato para desejar felicidades! Que hoje, dia {data_aniversario.strftime('%d/%m/%Y')} seja memorável na sua vida! Parabéns!"
    link_mensagem_whatsapp = f'https://api.whatsapp.com/send?phone={numero_telefone}&text={quote(mensagem)}'
    webbrowser.open(link_mensagem_whatsapp)
    sleep(5)
    seta = pyautogui.locateCenterOnScreen(r'C:\Users\lucas\Projetos\euvendedor\images\botao_iniciar_Conversa_whatsapp.png')
    sleep(3)
    pyautogui.click(seta[0], seta[1])
    sleep(1)
    seta = pyautogui.locateCenterOnScreen(r'C:\Users\lucas\Projetos\euvendedor\images\botao_usar_whatsapp_Web.png')
    sleep(5)
    pyautogui.click(seta[0], seta[1])
    sleep(20)
    seta = pyautogui.locateCenterOnScreen(r'C:\Users\lucas\Projetos\euvendedor\images\botao_enviar_whatsapp.png')
    sleep(20)
    pyautogui.click(seta[0], seta[1])
    sleep(10)
    pyautogui.hotkey('ctrl', 'w')
    sleep(7)