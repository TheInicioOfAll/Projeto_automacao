import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.alert('O código vai começar. Não use o computador até a mensagem final.')

produtos = []
produtos2 = []

with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        colunas = linha.split(' ')
        if colunas[0].strip():
            produtos.append(colunas[0].strip())

        if len(colunas) >= 2 and colunas[1].strip():
            produtos2.append(colunas[1].strip())

    for produto, produto2 in zip(produtos, produtos2):

        pyautogui.click(380, 462, duration=0.5)
        pyautogui.write(produto)
        pyautogui.press('enter')

        pyautogui.click(1333,712, clicks = 2)
        pyautogui.write(produto2)
        pyautogui.press('tab')

pyautogui.alert('O programa finalizou.')
