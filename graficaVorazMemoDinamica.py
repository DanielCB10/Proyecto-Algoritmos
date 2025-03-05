import matplotlib.pyplot as plt
import random

denominaciones = [25, 10, 5, 1]
print("Denominaciones generadas:", denominaciones)

# Algoritmo de programación dinámica
def min_monedas_dinamica(denominaciones, D):
    dp = [float('inf')] * (D + 1)
    dp[0] = 0
    for i in range(1, D + 1):
        for d in denominaciones:
            if d <= i:
                dp[i] = min(dp[i], dp[i - d] + 1)
    return dp[D]

# Algoritmo de divide y conquista con memoización
def min_monedas_DyCMemoizacion(denominaciones, D, memo=None):
    if memo is None:
        memo = {}

    if D == 0:
        return 0
    if D < 0:
        return float('inf')
    if D in memo:
        return memo[D]
    
    min_monedas = float('inf')
    for d in denominaciones:
        monedas = min_monedas_DyCMemoizacion(denominaciones, D - d, memo)
        if monedas != float('inf'):
            min_monedas = min(min_monedas, monedas + 1)
    
    memo[D] = min_monedas
    return min_monedas

# Algoritmo voraz
def min_monedas_voraz(denominaciones, D):
    denominaciones.sort(reverse=True)
    num_monedas = 0
    for d in denominaciones:
        while D >= d:
            D -= d
            num_monedas += 1
    return num_monedas

# Valores de D para probar
valores_D = range(1000, 10001, 5)

# Listas para almacenar los resultados
monedas_dinamica = []
monedas_memoizacion = []
monedas_voraz = []

for D in valores_D:
    monedas_dinamica.append(min_monedas_dinamica(denominaciones, D))
    monedas_memoizacion.append(min_monedas_DyCMemoizacion(denominaciones, D))
    monedas_voraz.append(min_monedas_voraz(denominaciones, D))

# Crear una figura con 3 subgráficas
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Gráfica de Programación Dinámica
axs[0].plot(valores_D, monedas_dinamica, label='Programación Dinámica', color='blue')
axs[0].set_ylabel('Número de monedas')
axs[0].legend()
axs[0].grid(True)

# Gráfica de Divide y Conquista con Memoización
axs[1].plot(valores_D, monedas_memoizacion, label='Divide y Conquista con Memoización', color='green')
axs[1].set_ylabel('Número de monedas')
axs[1].legend()
axs[1].grid(True)

# Gráfica del Algoritmo Voraz
axs[2].plot(valores_D, monedas_voraz, label='Voraz', color='red')
axs[2].set_ylabel('Número de monedas')
axs[2].legend()
axs[2].grid(True)

# Mostrar las gráficas
plt.tight_layout()
plt.show()
plt.close()