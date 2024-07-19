import pandas as pd

caminho_absoluto = r'C:\Users\lucas\Projetos\euvendedor\aniversarioclienteschevrolet.xlsx'
planilha = pd.read_excel(caminho_absoluto)

for indice, linha in planilha.iterrows():
        nome = linha[0]
        numero_telefone = linha[1]
        data_aniversario = linha[2]
        print(indice, linha)
