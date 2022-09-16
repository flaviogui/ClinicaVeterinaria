import os
from dados import *
from validacao import *

def menuProprietarios(proprietarios):
  os.system('clear')
  print('''
        -=- MENU PROPRIETÁRIOS -=-
        [1] - CADASTRAR PROPRIETÁRIO
        [2] - PESQUISAR PROPRIETÁRIO
        [3] - EDITAR PROPRIETÁRIO 
        [4] - EXCLUIR PROPRIETÁRIO 
        [5] - VOLTAR AO MENU PRINCIPAL
        ''')
  p = input('Digite sua opção: ')
  options_proprietarios(p,proprietarios)

def cadastrar_proprietario(proprietarios):
  print('Informe os dados abaixo.')
  nome = input('Digite o nome do proprietário: ')
  while invalid_name(nome):
    print('Nome inválido!')
    nome = input('Digite novamente o nome: ')
  email = input('Digite o email: ')
  tel = input('Digite o telefone: ')
  while invalid_int(tel):
    print('Telefone inválido!')
    tel = input('Digite novamente seu telefone: ')
  cpf = input('Digite o CPF do proprietário: ')
  while not validar_cpf(cpf):
    print('CPF inválido!')
    cpf = input('Digite novamente o CPF do proprietário: ')
  proprietarios[email] = [nome,tel,[],cpf]
  alterar_dados("proprietarios.dat",proprietarios)
  print('Proprietário cadastrado com sucesso!')

def pesquisar_proprietario(proprietarios):
  print("Informe o email do proprietário:")
  email = input()
  try:
    print(f"""
      Nome: {proprietarios[email][0]}
      Telefone: {proprietarios[email][1]}
      CPF do Proprietário: {proprietarios[email][3]}  """)
    for i in proprietarios[email][2]:
      print(f"\t  Animal:{i}")
    print()
  except:
    print("Proprietário não encontrado!")


def editar_proprietario(proprietarios):
  email = input("Informe o email do proprietario: ")
  
  aux = input("Desejar alterar o nome [S/N]: ")
  if aux == "S" or 's':
    nome = input("Informe nome: ")
    while invalid_name(nome):
      print("Nome incorreto")
      nome = input("Informe novamente o nome: ")
    proprietarios[email][0] = nome
    print("Nome alterado com sucesso")
    input("Tecle ENTER para continuar")
    
  os.system("clear")
  aux = input("Desejar alterar o telefone[S/s]: ")
  if aux == "s" or aux == 'S':
    telefone = input("Informe o novo número: ")
    while invalid_int(telefone):
      print("Telefone incorreto")
      telefone = input("Informe novamente o novo número: ")
    proprietarios[email][1] = telefone
    print("Telefone alterado com sucesso")
    input("Tecle ENTER para continuar")
    
  os.system("clear")
  alterar_dados('proprietarios.dat',proprietarios)

def excluir_proprietario(proprietarios):
  email = input("Informe o email do proprietário: ")
  try:
    proprietarios.pop(email)
    alterar_dados('proprietarios.dat',proprietarios)
  except:
    print("Email do proprietário informado inexistente!")
    
def options_proprietarios(op2,proprietarios):
  if op2 == '1':
    print('MENU CADASTRAR PROPRIETÁRIO')
    cadastrar_proprietario(proprietarios)
  elif op2 == '2':
    print('MENU PESQUISAR PROPRIETÁRIO')
    pesquisar_proprietario(proprietarios)
  elif op2 == '3':
    print('MENU EDITAR INFORMAÇÕES DO PROPRIETÁRIO')
    editar_proprietario(proprietarios)
  elif op2 == '4':
    print('MENU DE EXCLUIR PROPRIEÁRIO')
    excluir_proprietario(proprietarios)
  elif op2 == "5":
    return
  input('Tecle ENTER para continuar')
  menuProprietarios(proprietarios)