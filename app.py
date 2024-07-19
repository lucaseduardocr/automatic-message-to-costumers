import pandas as pd
import pyautogui
from tkinter import *
import webbrowser
import datetime
from time import sleep
from urllib.parse import quote


images = (r'C:\Users\lucas\Projetos\euvendedor\images\botao_enviar_whatsapp.png')

caminho_absoluto = r'C:\Users\lucas\Projetos\euvendedor\aniversarioclienteschevrolet.xlsx'
planilha = pd.read_excel(caminho_absoluto)


def data_atual():
    data_atual = datetime.date.today()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y")
    return data_atual_formatada      


def aniversario():
    for indice, linha in planilha.iterrows():
        nome = linha[0]
        numero_telefone = linha[1]
        data_aniversario2 = linha[2]
        data_aniversario2_formatada = data_aniversario2.strftime("%d/%m/%Y")
        data_atual()
        if data_aniversario2_formatada != data_atual():
            pass
        else:
            data_aniversario2_formatada == data_atual()
            nome_iterado = nome
            numero_telefone_iterado = numero_telefone
            data_aniversario_iterada = data_aniversario2_formatada
            return aniversario_whatsapp(nome_iterado, numero_telefone_iterado, data_aniversario_iterada)
            


def aniversario_whatsapp(nome_iterado, numero_telefone_iterado, data_aniversario_iterada):
    webbrowser.open('https://web.whatsapp.com/')
    sleep(15)
    mensagem = f"Olá {nome_iterado}, aqui é o Lucas da Jorlan, tudo bem ? Reparei aqui que hoje é seu aniversário! Entrando em contato para desejar felicidades! Que hoje, dia {data_aniversario_iterada} seja memorável na sua vida! Parabéns!"
    link_mensagem_whatsapp = f'https://api.whatsapp.com/send?phone={numero_telefone_iterado}&text={quote(mensagem)}'
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

aniversario()
