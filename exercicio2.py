def is_anagram(lista):
  lista = lista.lower()
  palavras = []
  palavra1 = []
  palavra2 = []
  palavras = lista.split()

  for i in range(len(palavras[0])):
    palavra1.append(palavras[0][i])

  for i in range(len(palavras[1])):
    palavra2.append(palavras[1][i])

  palavra1.sort()
  palavra2.sort()
  if(palavra1 == palavra2):
    return True
  else:
    return False











