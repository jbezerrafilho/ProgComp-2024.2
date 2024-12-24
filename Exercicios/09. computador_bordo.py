# Autor: José Bezerra
import math

tempo = float(input('Tempo gasto de viagem em minutos? '))
consumo_litros = float(input('Consumo em litros? '))
preco_gasolina = float(input('Preço do litro de gasolina em R$? '))
distancia = float(input('Distancia percorrida em Km? '))

#Convertendo o tempo em minutos em horas
tempo = tempo / 60

#Calculando velocidade média
velocidade_media = distancia / tempo

#Calculando desempenho do carro em km/litros e R$/Km
desempenho  = distancia / consumo_litros
custo_por_km = (consumo_litros * preco_gasolina) / distancia

#Calculando o custo da viagem
custo_da_viagem = (custo_por_km * distancia)

print(f'Dados de bordo: \n\
      Velocidade média: {velocidade_media:.2f} Km \n\
      Tempo de viagem: {tempo} horas. \n\
      Desempenho: {desempenho:.2f} Km/l \n\
      Custo por Km: {custo_por_km:.2f} R$/Km \n\
      Custo da viagem: R$ {custo_da_viagem:.2f}')