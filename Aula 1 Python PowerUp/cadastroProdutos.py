#Passo 1: entrar no sistema da empresa
import pyautogui
import time #usado pra sleep 

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 0.7 #pausa em segundos entre todos os comandos do pyautogui

#abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#entrar no site
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=492, y=359)
pyautogui.write("email")
pyautogui.press("tab")
#pyautogui.click(x=458, y=458) substitui a tecla tab acima
pyautogui.write("senha")
pyautogui.press("enter")
#pyautogui.click(x=658, y=510) substitui a tecla enter acima

time.sleep(3)

#Passo 3: Importar a base de dados
import pandas

listaprodutos = pandas.read_csv("Aula 1 Python PowerUp\produtos.csv")  # testar se vai funcionar 
print(listaprodutos)

#Passo 4: Cadastrar 1 produto
#Passo 5: Repetir o processo de cadastro até acabar
for linha in listaprodutos.index:          # for coluna in listaprodutos.columns se quisesse percorrer pelas colunas
    pyautogui.click(x=430, y=240)

    pyautogui.write(listaprodutos.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(listaprodutos.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(listaprodutos.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(listaprodutos.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(listaprodutos.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(listaprodutos.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = listaprodutos.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("enter")

    pyautogui.scroll(2000)