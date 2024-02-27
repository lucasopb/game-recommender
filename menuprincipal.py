import menuentrada
import pandas as pd
from time import sleep


def teste_prefenrencias(): 
    print('')



def main_menu():
    while True:
        print(f"bem vindo {menuentrada.usuarios[menuentrada.ind_perfil]['nome']}")
        sleep(1)
        resp = input("1 - fazer teste de preferencias\n2 - voltar\n")
        if resp == '1':
            teste_prefenrencias()
        if resp == '2':
            menuentrada.menu_entrada()
            


dataset_games = pd.read_csv("all_video_games(cleaned).csv")
print(dataset_games)


""" We mentioned in the chapter "A Brief 
Introduction to RPA" that one o
f the main features of RPA is 
that it is non-invasive. In other 
words, although RPA works with other 
software programs, it does not
require them to provide a special
interface. Instead, it directly 
interacts with the user interface of 
other software prog
rams to simulate human interactions.  """