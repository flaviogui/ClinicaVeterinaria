import os
from dados import *
from validacao import *


def menuAnimais(animais):
    os.system('clear')
    print('''
        -=- MENU ANIMAIS -=- 
        [1] - CADASTRAR ANIMAL 
        [2] - PESQUISAR ANIMAL
        [3] - EDITAR ANIMAL
        [4] - EXCLUIR ANIMAL
        [5] - VOLTAR AO MENU PRINCIPAL
        ''')
    p = input('Digite sua opção: ')
    options_animais(p, animais)


def cadastrar_animais(animais):
    print('Informe os dados abaixo')
    proprietario = conectar_dados("proprietarios.dat")
    email = input('Digite o email do dono do animal: ')
    if email not in proprietario:
        print("Proprietario inexistente")
        return
    nome = input('Digite o nome do animal: ')
    while invalid_name(nome):
        print("Nome incorreto!")
        nome = input('Digite novamente o nome do animal: ')
    raca = input('Qual a raça: ')
    idade = input('Digite a idade do animal: ')
    while invalid_int(idade):
        print("Idade incorreta!")
        idade = input('Digite novamente a idade do animal: ')
    porte = input('Qual o porte do animal: ')
    especie = input('Qual a espécie do animal: ')
    cor = input('Digite a cor do animal: ')
    animais[email + "|" + nome] = [nome, raca, idade, porte, especie, cor]
    proprietario[email][2].append(nome)
    alterar_dados("proprietarios.dat", proprietario)
    alterar_dados("animais.dat", animais)
    print('Animal cadastrado com sucesso!')


def pesquisar_animal(animal):
    print("Informe o email do proprietário: ")
    proprietario = conectar_dados("proprietarios.dat")
    email = input()
    if email not in proprietario:
        print("Proprietario inexistente!")
        return
    nome = input("Informe o nome do animal: ")
    try:
        print(f"""
          Nome do Animal: {animal[email+"|"+nome][0]}
          Raça: {animal[email+"|"+nome][1]}
          Idade: {animal[email+"|"+nome][2]}
          Porte:  {animal[email+"|"+nome][3]}
          Espécie: {animal[email+"|"+nome][4]}
          Cor: {animal[email+"|"+nome][5]}
          """)
    except:
        print("Animal não encontrado!")


def editar_animal(animal):
    email = input("Informe o email do proprietário: ")
    nome = input("Informe o nome do animal: ")
    if email + "|" + nome not in animal:
        print("Animal inexistente!")
        return
    os.system("clear")
    aux = input("Desejar alterar a idade do animal[S/s]: ")
    if aux == "s" or aux == 'S':
        idade = input("Informe a nova idade do animal: ")
        while invalid_int(idade):
            print("Incorreto, informe novamente!")
            idade = input("Informe novamente a idade do animal:")
        animal[email + "|" + nome][2] = idade
        print("Idade alterada com sucesso")
        input("Tecle ENTER para continuar")

    os.system("clear")
    aux = input("Desejar alterar o porte do animal[S/s]:")
    if aux == "s" or aux == 'S':
        porte = input("Informe o novo porte do seu animal: ")
        animal[email + "|" + no me][3] = porte
        print("Porte alterado com sucesso")
        input("Tecle ENTER para continuar")
    alterar_dados('animais.dat', animal)


def excluir_animal(animal):
    email = input("Informe o email do proprietario:")
    nome = input("Informe o nome do animal:")
    try:
        animal.pop(email + "|" + nome)
        alterar_dados('animais.dat', animal)
    except:
        print("Animal informado não existe")


def options_animais(op3, animais):
    if op3 == '1':
        print('MENU CADATRAR ANIMAL')
        cadastrar_animais(animais)
    elif op3 == '2':
        print('MENU PESQUISAR ANIMAL')
        pesquisar_animal(animais)
    elif op3 == '3':
        print('MENU EDITAR ANIMAL')
        editar_animal(animais)
    elif op3 == '4':
        print('MENU EXCLUIR ANIMAL')
        excluir_animal(animais)
    elif op3 == "5":
        return
    input("Tecle ENTER para continuar")
    op3 = menuAnimais(animais)
