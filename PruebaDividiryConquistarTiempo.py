from dividirConquistar import min_monedas_divide_conquistar

denominacionesPequeño = [1, 2, 5, 10]
DPequeño = 15

denominacionesMediano = [1, 2, 5, 10, 20]
DMedio = 35

denominacionesGrande = [1, 2, 5, 10, 20, 50]
DGrande = 88

denominacionesExtraGrande = [1, 2, 5, 10, 20, 50, 100]
DExtraGrande = 422
 

min_monedas1, tiempo1 = min_monedas_divide_conquistar(denominacionesPequeño, DPequeño)
print(f"Minimo de monedas para tamaño Pequeño: {min_monedas1} || Tiempo de ejecucion: {tiempo1} segundos")
min_monedas2, tiempo2 = min_monedas_divide_conquistar(denominacionesMediano, DMedio)
print(f"Minimo de monedas para tamaño Pequeño: {min_monedas2} || Tiempo de ejecucion: {tiempo2} segundos")
min_monedas3, tiempo3 = min_monedas_divide_conquistar(denominacionesGrande, DGrande) 
print(f"Minimo de monedas para tamaño Pequeño: {min_monedas3} || Tiempo de ejecucion: {tiempo3} segundos")
min_monedas4, tiempo4 = min_monedas_divide_conquistar(denominacionesExtraGrande, DExtraGrande) 
print(f"Minimo de monedas para tamaño Pequeño: {min_monedas4} || Tiempo de ejecucion: {tiempo4} segundos")







