import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))
def a():
  return(str())
print(diz_o_tipo("Alô"))
print(diz_o_tipo(15))
print(diz_o_tipo([1,2,3]))
print(diz_o_tipo(3.14))
print(diz_o_tipo({"nome":"joao"}))
print(diz_o_tipo(len)) 
