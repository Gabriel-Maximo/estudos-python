def divide_colunas(lista1, lista2):
  if len(lista1) != len(lista2):
      raise ValueError('As listas nao possuem o mesmo tamanho')

  divisao = []
  for pressao, temperatura in zip(lista1,lista2):
      resultado = pressao / temperatura
      divisao.append(resultado)
  return divisao 

pressoes = [100, 120, 140, 160, 180]
temperaturas = [1, 25, 30, 35, 40, 60]

try:
    resultado = divide_colunas(pressoes, temperaturas)
    print(resultado)

except ValueError as erro:
    print(erro)

except ZeroDivisionError as erro:
    print(erro)
