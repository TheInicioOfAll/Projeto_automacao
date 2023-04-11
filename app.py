import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.alert('O código vai começar. Não use o computador até a mensagem final.')

produtos = []


with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        colunas = linha.split(' ')
        if colunas[0].strip():
            produtos.append(colunas[0].strip())




    for produto in produtos:

        pyautogui.click(380, 462, duration=0.5)
        pyautogui.write(produto)
        pyautogui.press('enter')


time.sleep(2)



pyautogui.alert('O programa finalizou.')