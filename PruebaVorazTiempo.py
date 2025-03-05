from voraz import min_monedas_voraz

denominacionesPequeño = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
DPequeño = 24599

denominacionesMediano = [1] 
for i in range(2, 200, 2):  
    denominacionesMediano.append(i)
DMediano = 359543

denominacionesGrande = [1] 
for i in range(2, 2000, 2):  
    denominacionesGrande.append(i)
DGrande = 9380353292

denominacionesExtraGrande = [1] 
for i in range(2, 1000000, 2):  
    denominacionesGrande.append(i)
DExtraGrande = 10**14   

pequeño,tiempoPequeño = min_monedas_voraz(denominacionesPequeño, DPequeño)
mediano,tiempoMediano = min_monedas_voraz(denominacionesMediano, DMediano)
grande,tiempoGrande = min_monedas_voraz(denominacionesGrande, DGrande)
extragrande,tiempoExtraGrande = min_monedas_voraz(denominacionesGrande, DExtraGrande)


print(f"Monedas para tamaño Pequeño: {pequeño}",f" || Tiempo de ejecución: {tiempoPequeño:.6f} segundos" )
print(f"Monedas para tamaño Mediano: {mediano} ", f" || Tiempo de ejecución : {tiempoMediano:.6f} segundos")
print(f"Monedas para tamaño Grande: {grande} ", f" || Tiempo de ejecución : {tiempoGrande:.6f} segundos")
print(f"Monedas para tamaño ExtraGrande: {extragrande} ",f" || Tiempo de ejecución|: {tiempoExtraGrande:.6f} segundos")





