import matplotlib.pyplot as plt

def min_monedas_dinamica(denominaciones, D):
    contador = 0  # Contador de operaciones
    dp = [float('inf')] * (D + 1)  # Tabla DP
    dp[0] = 0  
    for i in range(1, D + 1):
        for d in denominaciones:
            contador += 1  # Cada comparación y operación cuenta como una operación
            if d <= i:
                dp[i] = min(dp[i], dp[i - d] + 1)
    return dp[D], contador  

# Denominaciones de monedas
denominaciones = [25, 10, 5, 1]

# Valores de D para probar
valores_D = range(1, 10000)

# Listas para almacenar los resultados
num_monedas_lista = []
operaciones_lista = []

for D in valores_D:
    num_monedas, operaciones = min_monedas_dinamica(denominaciones, D)
    num_monedas_lista.append(num_monedas)
    operaciones_lista.append(operaciones)

# Gráfica
plt.figure(figsize=(10, 6))

# Gráfica de la cantidad de monedas
plt.subplot(2, 1, 1)
plt.plot(valores_D, num_monedas_lista, label='Número de monedas', color='blue')
plt.xlabel('Valor de D')
plt.ylabel('Número de monedas')
plt.title('Número de monedas vs Valor de D (Programación Dinámica)')
plt.legend()

# Gráfica de la cantidad de operaciones
plt.subplot(2, 1, 2)
plt.plot(valores_D, operaciones_lista, label='Número de operaciones', color='red')
plt.xlabel('Valor de D')
plt.ylabel('Número de operaciones')
plt.title('Número de operaciones vs Valor de D (Programación Dinámica)')
plt.legend()

plt.tight_layout()
plt.show()
plt.close()