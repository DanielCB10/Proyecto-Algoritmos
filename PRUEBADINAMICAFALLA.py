from programacionDinamica import min_monedas_dinamica

denominaciones = [1, 3, 4]
# Cantidad a devolver
D = 6

# Llamada al algoritmo voraz
resultado = min_monedas_dinamica(denominaciones, D)
print(f"Número de monedas devueltas: {resultado}")