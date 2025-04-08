import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv('dados.csv')

# Cria um gráfico de barras
plt.bar(df['nome'], df['valor'])

# Adiciona título
plt.title('Valores por Nome')

# Salva o gráfico como imagem
plt.savefig('grafico.png')

print("Gráfico gerado com sucesso!")
