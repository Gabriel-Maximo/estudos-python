gabarito = ['D', 'A', 'B', 'C', 'A']

testes_sem_ex = [
    ['D', 'A', 'B', 'C', 'A'],
    ['C', 'A', 'A', 'C', 'A'],
    ['D', 'B', 'A', 'C', 'A']
]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

notas = []
for teste in testes_com_ex:
  nota = 0
  for indice, resposta in enumerate(teste):
    if resposta == gabarito[indice]:
      nota += 1
    if resposta not in ['A', 'B', 'C', 'D']:
      raise ValueError(f'A alternativa {resposta} não é uma opção de alternativa válida')
  notas.append(nota)
print(notas)
