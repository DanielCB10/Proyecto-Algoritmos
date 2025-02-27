from DyCMemoizacion import min_monedas_DyCMemoizacion

denominacionesPequeño = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
DPequeño = 920
operaciones = []

memo={}
print(f"El número mínimo de monedas es: {min_monedas_DyCMemoizacion(denominacionesPequeño, DPequeño, memo,operaciones)}")
print(f"Operaciones realizadas: {operaciones[0]}")


