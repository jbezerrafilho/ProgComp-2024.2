import yfinance as yf
import matplotlib.pyplot as plt

ticker = 'PETR4.SA'
df = yf.download( ticker,  period='1y')

#Criar o gráfico
plt.plot(df.index, df["Close"], "purple")

# Configurações do gráfico
plt.title(f"Histórico de Preços - {ticker}")
plt.xlabel("Data")
plt.ylabel("Preço (R$)")
plt.xticks(rotation=45)

# Mostrar o gráfico
plt.show()

