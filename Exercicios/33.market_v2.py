import yfinance as yf
import matplotlib.pyplot as plt
from pprint import pprint

ticker = 'PETR4.SA'
df = yf.download( ticker,  period='5mo')

# Dicionário dados
dados = df['Close'].to_dict()
pprint(dados)

datas = list(dados[ticker].keys())
precos = list(dados[ticker].values())



#Criar o gráfico
plt.plot(datas, precos, color="purple")

# Configurações do gráfico
plt.title(f"Histórico de Preços - {ticker}")
plt.xlabel("Data")
plt.ylabel("Preço (R$)")
plt.xticks(rotation=45)
plt.grid(True)

# Mostrar o gráfico
plt.show()

