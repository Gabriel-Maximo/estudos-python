lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',

                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',

                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
                  
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',

                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',

                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

def verificar_pontuacao():
  for palavra in lista_nao_tratada:
    if '!'in palavra or '?' in palavra or ',' in palavra or '.' in palavra:
      raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}"')
verificar_pontuacao()
