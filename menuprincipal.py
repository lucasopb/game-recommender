import menuentrada
import pandas as pd
from time import sleep
import ast

dataset_games = pd.read_csv('all_video_games(cleaned).csv')

def pergunta1():
    gens_escolhidos = []
    print('digite dentre esses seus tres generos de jogos favoritos\n(Action, Adventure, RPG, FPS, Sports, Racing, Strategy, Puzzle')
    gens_escolhidos.append(input('1.'))
    gens_escolhidos.append(input('2.'))
    gens_escolhidos.append(input('3.'))
    return gens_escolhidos


def pergunta2():
    plataformas_escolhidas = []
    plataforma = input('digite a plataforma de jogos que voce tem preferencia para jogar\n')
    dataset_games['Platforms Info'] = dataset_games['Platforms Info'].apply(ast.literal_eval)
    conf = 0
    for element_info in dataset_games['Platforms Info']: 
        for platform_info in element_info:
            if platform_info['Platform'] == plataforma:
                conf = 1
        if conf == 1:
            plataformas_escolhidas.append(element_info)
            conf = 0
    return plataformas_escolhidas


def pergunta3():
        nota_min = 0
        resposta = input("voce se considera uma pessoa muito critica em relaçao a jogos?(sim/nao)\n").lower()
        if resposta == "sim":
            nota_min = 7
        return nota_min


def teste_prefenrencias():
        print('agora ira começar um questionario para entendermos suas preferencias\n')
        sleep(1)

        gens_escolhidos = pergunta1()
        plataformas_escolhidas = pergunta2()
        nota_min = pergunta3()  

        dataset_filtered = dataset_games.loc[
        dataset_games['Genres'].isin(gens_escolhidos) &
        dataset_games['Platforms Info'].isin(plataformas_escolhidas) &
        (dataset_games['User Score'] > nota_min)
        ]

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