import yfinance as yf
import matplotlib.pyplot as plt
import mplcursors  # Importe a biblioteca mplcursors

# Baixar os dados do ativo
ticker = 'PETR4.SA'
df = yf.download(ticker, period='1y')

df.to_csv()

# # Criar o gráfico
# plt.plot(df.index, df["Close"], color="purple")

# # Configurações do gráfico
# plt.title(f"Histórico de Preços - {ticker}")
# plt.xlabel("Data")
# plt.ylabel("Preço (R$)")
# plt.xticks(rotation=45)
# plt.grid(True)

# # Habilitar o cursor flutuante
# mplcursors.cursor(hover=True)

# # Mostrar o gráfico
# plt.tight_layout()
# plt.show()