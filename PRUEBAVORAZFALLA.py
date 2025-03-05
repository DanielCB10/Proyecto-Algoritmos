from voraz import min_monedas_voraz

denominaciones = [1, 3, 4]
# Cantidad a devolver
D = 6

# Llamada al algoritmo voraz
resultado = min_monedas_voraz(denominaciones, D)
print(f"Número de monedas devueltas: {resultado}")

