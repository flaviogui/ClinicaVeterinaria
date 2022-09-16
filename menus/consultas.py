import os
from dados import *
from validacao import *

def menuConsultas(consultas):
  os.system('clear')
  print('''
        -=- MENU CONSULTAS -=-
        [1] - MARCAR CONSULTA
        [2] - PESQUISAR CONSULTA 
        [3] - REMARCAR CONSULTA
        [4] - CANCELAR CONSULTA
        [5] - VOLTAR AO MENU PRINCIPAL
        ''')
  p = input('Digite sua opção: ')
  options_consultas(p,consultas)

def cadastrar_consulta(consulta):
  print('Informe os dados abaixo')
  email = input('Digite o email do cliente: ')
  especie = input('Digite a espécie do animal: ')
  nome_animal = input('Digite o nome do animal: ')
  while invalid_name(nome_animal):
    print('incorreto')
    nome_animal = input('Digite novamente o nome do animal: ')
  nome = input('Digite o nome do cliente: ')
  while invalid_name(nome):
    print('incorreto')
    nome = input('Digite novamente o nome do cliente: ')
  data = input('Digite a data da consulta: ')
  while invalid_data(data):
    print("incorreto")
    data = input('Digite novamente a data da consulta: ')
  horario = input('Digite o horário da consulta: ')
  while invalid_hora(horario):
    print('incorreto')
    horario = input('Digite novamente o horário da consulta: ')
  veterinario = input('Digite o nome do veterinário: ')
  patologia = input('O que o animal está sentido: ')
  vacinas = input('As vacinas estão em dia [SIM] ou [NÃO]: ')
  while vacinas != 'NÃO' and vacinas != 'SIM':
    print('incorreto')
    vacinas = input('As vacinas estão em dia [SIM] ou [NÃO]: ')
  consulta[email] = [nome,especie,nome_animal,data,horario,veterinario,patologia,vacinas]
  alterar_dados("consultas.dat",consulta)
  print('Consulta cadastrada com sucesso!')

def pesquisar_consulta(consulta):
  print("Informe o email do cliente:")
  email = input()
  if email in consulta:
    print(f"""
          Nome do cliente: {consulta[email][0]}
          Espécie do Animal: {consulta[email][1]}
          Nome do Animal: {consulta[email][2]}
          Data: {consulta[email][3]}
          Horas: {consulta[email][4]}
          Veterinário: {consulta[email][5]}
          Sintomas do animal: {consulta[email][6]}
          Vacinas em dia: {consulta[email][7]}
          """)
  else:
    print("Consulta não encontrada")


def adiar_consulta(consulta):
  email = input("Informe o email do proprietário:")
  if email not in consulta:
    print("Consulta inexistente!")
    return
  if email in consulta:
    aux = input("Desejar alterar a data e horário da consulta [S/N]: ")
    if aux == 's' or 'S':
      data = input('Informe a nova data da consulta: ')
      while invalid_data(data):
        print('Data incorreta!')
        data = input('Informe novamente a nova data da consulta: ')
      consulta[email][3] = data
      horario = input('Agora, informe a nova hora: ')
      while invalid_hora(horario):
        print('Hora incorreta!')
        horario = input('Informe novamente a nova hora: ')
      consulta[email][4] = horario
      print('Consulta remarcada com sucesso!')
      
    alterar_dados('consultas.dat',consulta)
  else:
    print("Esse cliete não possui consulta marcada!")
def excluir_consulta(consulta):
  email = input("Informe o email do cliente:")
  try:
    consulta.pop(email)
    alterar_dados('consultas.dat',consulta)
    print('Consulta excluída com sucesso!')
  except:
    print("Consulta inexistente!")

def options_consultas(op4,consultas):
  if op4 == '1':
    print('MENU MARCAR CONSULTA')
    cadastrar_consulta(consultas)
  elif op4 == '2':
    print('MENU PESQUISAR CONSULTAS')
    pesquisar_consulta(consultas)
  elif op4 == '3':
    print('MENU REMARCAR CONSULTA')
    adiar_consulta(consultas)
  elif op4 == '4':
    print('MENU CANCELAR CONSULTA')
    excluir_consulta(consultas)
  elif op4 == "5":
    return
  input("Tecle ENTER para continuar")
  menuConsultas(consultas)
  
