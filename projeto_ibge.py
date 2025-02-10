import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Garantir que os pacotes necessários estão instalados
try:
    import pandas
    import matplotlib
    import seaborn
except ModuleNotFoundError as e:
    print(f"Erro: {e}. Certifique-se de instalar os pacotes necessários usando: pip install pandas matplotlib seaborn")
    raise

# Carregar dados (exemplo fictício, substitua pelo real)
data = {
    'Ano': [2018, 2019, 2020, 2021, 2022, 2023],
    'Taxa_Desemprego': [12.3, 11.9, 13.5, 14.7, 12.1, 9.8]
}
df = pd.DataFrame(data)

# Exibir primeiras linhas
print(df.head())  # Substituindo display() por print() para compatibilidade geral

# Criar um gráfico de linha
plt.figure(figsize=(8,5))
sns.lineplot(x='Ano', y='Taxa_Desemprego', data=df, marker='o', linestyle='-')
plt.title('Taxa de Desemprego no Brasil (2018-2023)')
plt.xlabel('Ano')
plt.ylabel('Taxa de Desemprego (%)')
plt.grid(True)
plt.show()
