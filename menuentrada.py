import sys

usuarios = []

def fazer_login():
    while True:
        nome_perfil = input("Digite o nome do perfil ou digite (0) para voltar: ").capitalize()
        if nome_perfil == '0':
            break
        for i, element in enumerate(usuarios):
            if nome_perfil == element['nome']:
                senha = input("Digite a sua senha: ")
                if senha == element['senha']:
                    global ind_perfil
                    ind_perfil = i
                    print(f"bem vindo {element['nome']}")
                    return True
                else:
                    print("Senha incorreta, tente novamente.")
                    break
            else:
                print("Nome invalido, tente novamente")
        else:
            print("\nPerfil inválido, tente novamente.\n")


def cadastrar_usuario():
    while True:
        perfil = {'nome': input("Digite o nome do perfil ou digite (0) para voltar: ").capitalize()}
        if perfil['nome'] == '0':
            break
        for element in usuarios:
            if perfil['nome'] == element['nome']:
                print("\nO perfil já cadastrado! Tente novamente.\n")
        else:
            senha = input("Digite a sua senha: ")
            perfil['senha'] = senha
            copia = perfil.copy()
            usuarios.append(copia)
            print("\nPerfil cadastrado com sucesso!\n")
            break


def menu_entrada():
    while True:
        print('---------------------------')
        print(' APP recomendador de jogos ')
        print('---------------------------')
        for i, element in enumerate(usuarios):
            print(f'Usuário {i + 1} - ' + element['nome'])
        escolha = input("\n1 - Cadastro de perfil\n2 - Login de perfil\n3 - Sair\n")

        if escolha == '1':
            cadastrar_usuario()
            
        if escolha == '2':
            if fazer_login():
                return True

        elif escolha == '3':
            sys.exit()
