import matplotlib.pyplot as plt

def min_monedas_DyCMemoizacion(denominaciones, D, memo, operaciones):
    min_monedas = float('inf')
    operaciones[0] += 1  # Contador de operaciones (inicialización de min_monedas)
    if D == 0:
        return 0
    if D < 0:
        return float('inf')
    if D in memo:
        return memo[D]
    for d in denominaciones:
        operaciones[0] += 1  # Contador de operaciones (comparación d <= D)
        monedas = min_monedas_DyCMemoizacion(denominaciones, D - d, memo, operaciones)
        operaciones[0] += 1  # Contador de operaciones (comparación monedas != float('inf'))
        if monedas != float('inf'):
            min_monedas = min(min_monedas, monedas + 1)
            operaciones[0] += 1  # Contador de operaciones (asignación de min_monedas)
    memo[D] = min_monedas
    return min_monedas

# Denominaciones de monedas
denominaciones = [25, 10, 5, 1]
# Valores de D para probar
valores_D = range(1, 1000)
# Listas para almacenar los resultados
num_monedas_lista = []
operaciones_lista = []
for D in valores_D:
    memo = {}  # Reiniciamos la memoización para cada D
    operaciones = [0]  # Reiniciamos el contador de operaciones para cada D
    num_monedas = min_monedas_DyCMemoizacion(denominaciones, D, memo, operaciones)
    num_monedas_lista.append(num_monedas)
    operaciones_lista.append(operaciones[0])

# Gráfica
plt.figure(figsize=(10, 6))
# Gráfica de la cantidad de monedas
plt.subplot(2, 1, 1)
plt.plot(valores_D, num_monedas_lista, label='Número de monedas', color='blue')
plt.xlabel('Valor de D')
plt.ylabel('Número de monedas')
plt.title('Número de monedas vs Valor de D (Divide y Conquista con Memoización)')
plt.legend()
# Gráfica de la cantidad de operaciones
plt.subplot(2, 1, 2)
plt.plot(valores_D, operaciones_lista, label='Número de operaciones', color='red')
plt.xlabel('Valor de D')
plt.ylabel('Número de operaciones')
plt.title('Número de operaciones vs Valor de D (Divide y Conquista con Memoización)')
plt.legend()
plt.tight_layout()
plt.show()
plt.close()