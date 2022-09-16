import pickle

def conectar_dados(path):
  retorno = {}
  try:
    file = open(path,'x')
    file.close()
    return retorno
  except:
    try:
      file = open(path,'rb')
      retorno = pickle.load(file)
      file.close()
      return retorno
    except:
      file.close()
      return retorno

def alterar_dados(path,dict):
  with open(path,'wb') as file:
    pickle.dump(dict,file)
