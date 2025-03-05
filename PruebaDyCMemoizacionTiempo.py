from DyCMemoizacion import min_monedas_DyCMemoizacion

denominacionesPequeño = [1, 2, 5, 10]
DPequeño = 15
memoPequeño={}

denominacionesMedio = [1, 2, 5, 10, 20]
DMedio = 35
memoMedio={}

denominacionesGrande = [1, 2, 5, 10, 20, 50]
DGrande = 88
memoGrande={}

denominacionesExtraGrande = [1, 2, 5, 10, 20, 50, 100,200]
DExtraGrande = 422
memoExtraGrande={}


min_monedas1, tiempo1 = min_monedas_DyCMemoizacion(denominacionesPequeño, DPequeño,memoPequeño)
print(f"Minimo de monedas para tamaño Pequeño: {min_monedas1} || Tiempo de ejecucion: {tiempo1} segundos")
min_monedas2, tiempo2 = min_monedas_DyCMemoizacion(denominacionesMedio, DMedio, memoMedio)
print(f"Minimo de monedas para tamaño Medio: {min_monedas2} || Tiempo de ejecucion: {tiempo2} segundos")
min_monedas3, tiempo3 = min_monedas_DyCMemoizacion(denominacionesGrande, DGrande,memoGrande ) 
print(f"Minimo de monedas para tamaño Grande: {min_monedas3} || Tiempo de ejecucion: {tiempo3} segundos")
min_monedas4, tiempo4 = min_monedas_DyCMemoizacion(denominacionesExtraGrande, DExtraGrande, memoExtraGrande) 
print(f"Minimo de monedas para tamaño ExtraGrande: {min_monedas4} || Tiempo de ejecucion: {tiempo4} segundos")


