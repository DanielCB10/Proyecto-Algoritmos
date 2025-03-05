import matplotlib.pyplot as plt

def min_monedas_divide_conquistar(denominaciones, D, contador=[0]):
    if D == 0:
        return 0, contador[0]
    min_monedas = float('inf')
    for d in denominaciones:
        contador[0] += 1  # Contador de operaciones (comparación d <= D)
        if d <= D:
            contador[0] += 1  # Contador de operaciones (llamada recursiva)
            subproblema, _ = min_monedas_divide_conquistar(denominaciones, D - d, contador)
            if subproblema + 1 < min_monedas:
                contador[0] += 1  # Contador de operaciones (asignación de min_monedas)
                min_monedas = subproblema + 1
    return min_monedas, contador[0]





# Denominaciones de monedas
denominaciones = [25, 10, 5, 1]
# Valores de D para probar 
valores_D = range(1, 39)  # Solo hasta 39 para evitar tiempos de ejecución muy largos
# Listas para almacenar los resultados
num_monedas_lista = []
operaciones_lista = []
for D in valores_D:
    contador = [0]  # Reiniciamos el contador para cada D
    num_monedas, operaciones = min_monedas_divide_conquistar(denominaciones, D, contador)
    num_monedas_lista.append(num_monedas)
    operaciones_lista.append(operaciones)
# Gráfica
plt.figure(figsize=(10, 6))
# Gráfica de la cantidad de monedas
plt.subplot(2, 1, 1)
plt.plot(valores_D, num_monedas_lista, label='Número de monedas', color='blue')
plt.xlabel('Valor de D')
plt.ylabel('Número de monedas')
plt.title('Número de monedas vs Valor de D (Divide y Conquista)')
plt.legend()
# Gráfica de la cantidad de operaciones
plt.subplot(2, 1, 2)
plt.plot(valores_D, operaciones_lista, label='Número de operaciones', color='red')
plt.xlabel('Valor de D')
plt.ylabel('Número de operaciones')
plt.title('Número de operaciones vs Valor de D (Divide y Conquista)')
plt.legend()
plt.tight_layout()
plt.show()
plt.close()