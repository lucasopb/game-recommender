import menuentrada
import pandas as pd
from time import sleep


dataset_games = pd.read_csv('all_video_games(cleaned).csv')
gens = ['Action', 'Adventure', 'RPG', 'FPS', 'Sports', 'Racing', 'Strategy', 'Puzzle']
dataset_games_filtered = dataset_games.loc[dataset_games['Genres'].isin(gens)]

def teste_prefenrencias():
    gens_escolhidos = [] 
    print('agora ira começar um questionario para entendermos suas preferencias\n')
    sleep(1)
    print('digite dentre esses seus tres generos de jogos favoritos\n(Action, Adventure, RPG, FPS, Sports, Racing, Strategy, Puzzle')
    gens_escolhidos.append(input('1.'))
    gens_escolhidos.append(input('2.'))
    gens_escolhidos.append(input('3.'))
    dataset_filtered = dataset_games_filtered.loc[dataset_games_filtered['Genres'].isin(gens_escolhidos)]
    print(dataset_filtered)


    



def main_menu():
    while True:
        print(f"bem vindo {menuentrada.usuarios[menuentrada.ind_perfil]['nome']}")
        sleep(1)
        resp = input("1 - fazer teste de preferencias\n2 - voltar\n")
        if resp == '1':
            teste_prefenrencias()
        if resp == '2':
            menuentrada.menu_entrada()
            



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