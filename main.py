import os
from dados import conectar_dados
from menus.proprietarios import menuProprietarios
from menus.animais import menuAnimais
from menus.consultas import menuConsultas
from menus.relatorios import menuRelatorios



def menuPrincipal():
  os.system('clear')
  print('\033[1;32m'+'''
      -=- BEM VINDOS AO AMBIENTE CLÍNICA VETERINÁRIA -=-
      
      [1] - MENU DOS PROPRIETÁRIOS DOS ANIMAIS
      [2] - MENU DOS ANIMAIS
      [3] - MENU DAS CONSULTAS
      [4] - MENU DOS RELATÓRIOS
      [5] - FINALIZAR PROGRAMA  
      [6] - CRÉDITOS DO PROJETO
      ''')
  p = input('DIGITE SUA OPÇÃO: ')
  return p
  
def creditos():
  print('''   
  Projeto: Clínica Veterinária
  Autores do Projeto:
  Flávio Glaydson G. Lopes; Mat.:(20220046917)
  Isayan Deivid N. Monteiro; Mat.:(20220043737)
  ''')
  input("Tecle ENTER para continuar")



op1 = menuPrincipal()
while op1 != '5':
  
  proprietarios = conectar_dados('proprietarios.dat')
  animais = conectar_dados('animais.dat')
  consultas = conectar_dados('consultas.dat')
  
  if op1 == '1':
    menuProprietarios(proprietarios)

  elif op1 == '2':
    menuAnimais(animais)

  elif op1 == '3':
    menuConsultas(consultas)
    
  elif op1 == '4':
    menuRelatorios(animais,consultas,proprietarios)

  elif op1 == '6':
    creditos()
    

  else:
    print('OPÇÃO INVÁLIDA!')
    print('Por favor, tente novamente')
    input('Tecle ENTER para continuar')
  op1 = menuPrincipal()

print('Fim do Programa, até logo!')
    
