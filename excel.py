import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.alert('NÃO MEXA NO COMPUTADOR, O PROGRAMA VAI COMEÇAR A RODAR.')

pyautogui.hotkey('alt', 'tab', duration = 1)

numero_de_repeticoes = 50

def funcao_para_repetir():
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

repeticao_atual = 0

while repeticao_atual != numero_de_repeticoes:
    repeticao_atual += 1
    funcao_para_repetir()


time.sleep(2)

pyautogui.alert('O PROGRAMA ACABOU, PODE VOLTAR A MEXER.')