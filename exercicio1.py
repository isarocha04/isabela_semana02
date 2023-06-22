def conta_palavras_unicas(lista):
  contador = 0
  lista = lista.lower()
  palavras=[]
  palavras = lista.split()
  for i in range(len(palavras)-1):
    if (palavras[i]!=palavras[i+1]):
      contador+=1
    else:
      contador = 1
  print(lista)
  return contador










