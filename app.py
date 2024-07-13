import pandas as pd
import pyautogui
import tkinter
import webbrowser
import datetime

data_atual = datetime.date.today()
data_atual_formatada = data_atual.strftime("%d/%m/%Y")


caminho_absoluto = r'C:\Users\lucas\Projetos\euvendedor\aniversarioclienteschevrolet.xlsx'

planilha = pd.read_excel(caminho_absoluto)

for indice, linha in planilha.iterrows():
    data_aniversario = linha[2]
    print(data_aniversario)
