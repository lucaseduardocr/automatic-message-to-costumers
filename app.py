import pandas as pd
import pyautogui


caminho_absoluto = '/root/projetosTESTE/projetos/euvendedor/euvendedor/aniversarioclienteschevrolet.xlsx'

planilha = pd.read_excel(caminho_absoluto)

print(planilha)

