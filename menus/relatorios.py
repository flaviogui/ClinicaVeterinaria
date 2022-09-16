import os


def menuRelatorios(animais,consultas,proprietarios):
  os.system('clear')
  print('''
        -=- MENU RELATÓRIO -=- 
        [1] - RELATÓRIO DE COMPLETO DOS PROPRIETÁRIOS
        [2] - RELATÓRIO DE COMPLETO DOS ANIMAL
        [3] - RELATÓRIO DE TODAS ÀS CONSULTAS
        [4] - VOLTAR AO MENU PRINCIPAL
        ''')
  p = input('Digite sua opção: ')
  options_relatorio(p,animais,consultas,proprietarios)

def relatorio_proprietarios(proprietarios):
  print("Relatório do proprietarios:")
  for key in proprietarios:
    print(f"""
      Nome do Proprietário: {proprietarios[key][0]}
      Email do Proprietário: {key}
      Telefone do Proprietário: {proprietarios[key][1]}
      CPF do Proprietário: {proprietarios[key][3]}""")
    for i in proprietarios[key][2]:
      print(f"\t  Animal:{i}")
    print()

def relatorio_animais(animais):
  print("Relatório dos animais")
  for key in animais:
    email = key.split("|")
    print(f"""
      Email do Proprietário: {email[0]}
      Nome do Animal: {animais[key][0]}
      Raça do Animal: {animais[key][1]}
      Idade do Animal: {animais[key][2]}
      Porte do Animal: {animais[key][3]}
      Espécie do Animal: {animais[key][4]}
      Cor do Animal: {animais[key][5]}
                 """)

def relatorio_consultas(consultas):
  print("relatorio de todas as consultas:")
  for key in consultas:
    print(f"""
      Nome do Cliente: {consultas[key][0]}
      Email do cliente: {key}
      Espécie do Animal: {consultas[key][1]}    
      Nome do Animal: {consultas[key][2]}
      Data da Consulta: {consultas[key][3]}
      Horário da Consulta: {consultas[key][4]}
      Nome do Veterinário: {consultas[key][5]}
      O que o animal está sentido: {consultas[key][6]}
      Vacinas em dia: {consultas[key][7]}  
          """)
    

   

def options_relatorio(op5,animais,consultas,proprietarios):
  if op5 == '1':
    print('MENU RELATÓRIO COMPLETO DOS PROPRIETÁRIOS')
    relatorio_proprietarios(proprietarios)
  if op5 == '2':
    print('MENU RELATÓRIO COMPLETO DOS ANIMAS')
    relatorio_animais(animais)
  if op5 == '3':
    print('MENU RELATÓRIO DAS CONSULTAS MARCADAS')
    relatorio_consultas(consultas)
  if op5 == "4":
    return
  input("Tecle ENTER para continuar")
  menuRelatorios(animais,consultas,proprietarios)
  