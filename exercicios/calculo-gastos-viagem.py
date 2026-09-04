def gastos_hotel():
  gastos_hotel = 150 * 3
  return gastos_hotel

lista_km = [850, 800, 300, 550]
def gastos_gasolina():
  distancia = lista_km[0] * 2
  litros = distancia / 14
  gastos_gasolina = litros * 5
  return gastos_gasolina

lista_passeio = [200, 400, 250, 300]
def gastos_passeio():
  gastos_passeio = lista_passeio[0] * 3
  return gastos_passeio

total = gastos_hotel() + gastos_gasolina() + gastos_passeio()
print(f'Com base nos gastos definidos, uma viagem de 3 dias para Salvador saindo de Recife custaria {total:.2f} reais')
