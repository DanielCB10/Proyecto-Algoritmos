from dividirConquistar import min_monedas_divide_conquistar

denominaciones = [1, 3, 4]
# Cantidad a devolver
D = 6

# Llamada al algoritmo voraz
resultado = min_monedas_divide_conquistar(denominaciones, D)
print(f"Número de monedas devueltas: {resultado}")

