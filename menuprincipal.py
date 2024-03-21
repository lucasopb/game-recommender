import menuentrada
import pandas as pd
from time import sleep
import ast


dataset_games = pd.read_csv('all_video_games(cleaned).csv')


def format_txt(texto):
    if len(texto) <= 3:
        return texto.upper()
    else:
        return texto.capitalize()
    

def mostrar_recomendaçoes(dataset):
    print("jogos recomendados:")
    for name in dataset['Title'].head(10):
        print(name)


def pergunta1():
    gens_escolhidos = []
    print('digite dentre esses seus tres generos de jogos favoritos\n(Action, Adventure, RPG, FPS, Sports, Racing, Strategy, Puzzle')
    gens_escolhidos.append(format_txt(input('1.')))
    gens_escolhidos.append(format_txt(input('2.')))
    gens_escolhidos.append(format_txt(input('3.')))
    return gens_escolhidos


# Ajeitar o Wii para WII (capitalizado)
# Deixar o PlayStation apenas capitalizado
def pergunta2():
    plataformas_escolhidas = []
    plataforma = input('digite a plataforma de jogos que voce tem preferencia para jogar?\n')
    dataset_games['Platforms Info'] = dataset_games['Platforms Info'].apply(ast.literal_eval)
    conf = 0
    for array_info in dataset_games['Platforms Info']: 
        for dict_info in array_info:
            if dict_info['Platform'] == plataforma:
                conf = 1
        if conf == 1:
            plataformas_escolhidas.append(array_info)
            conf = 0
    return plataformas_escolhidas


def pergunta3():
    nota_min = 0
    resposta = input("voce se considera uma pessoa muito critica em relaçao a jogos?(sim/nao)\n").lower()
    if resposta == "sim":
        nota_min = 7
    return nota_min


def pergunta4():
    faixa_etaria_escolhida = ["Rated E For Everyone", "Rated E +10 For Everyone +10"]
    idade = int(input("qual a sua idade?\n"))
    if idade > 12:
        faixa_etaria_escolhida.append('Rated T For Teen')
    if idade > 18:
        faixa_etaria_escolhida.append('Rated M For Mature')
    return faixa_etaria_escolhida



def teste_prefenrencias():
    print('agora ira começar um questionario para entendermos suas preferencias\n')
    sleep(1)

    gens_escolhidos = pergunta1()
    plataformas_escolhidas = pergunta2()
    nota_min = pergunta3()  
    faixa_etaria_escolhida = pergunta4()

    dataset_filtered = dataset_games.loc[
    dataset_games['Genres'].isin(gens_escolhidos) &
    dataset_games['Platforms Info'].isin(plataformas_escolhidas) &
    dataset_games['Product Rating'].isin(faixa_etaria_escolhida) &
    (dataset_games['User Score'] > nota_min)
    ]

    mostrar_recomendaçoes(dataset_filtered)


def main_menu():
    while True:
        sleep(1)
        print('---------------------------')
        print(' APP recomendador de jogos ')
        print('---------------------------')
        resp = input("1 - Fazer teste de preferencias\n2 - Sair\n")
        if resp == '1':
            teste_prefenrencias()
        if resp == '2':
            menuentrada.menu_entrada()