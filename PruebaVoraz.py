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

pequeño = min_monedas_voraz(denominacionesPequeño, DPequeño)
mediano = min_monedas_voraz(denominacionesMediano, DMediano)
grande = min_monedas_voraz(denominacionesGrande, DGrande)
extragrande = min_monedas_voraz(denominacionesGrande, DExtraGrande)


print("Numero de monedas:",pequeño,"  ,  ","Numero de operaciones:",pequeño)
print("Numero de monedas:",mediano,"  ,  ","Numero de operaciones:",mediano)
print("Numero de monedas:",grande,"  ,  ","Numero de operaciones:",grande)
print("Numero de monedas:",extragrande,"  ,  ","Numero de operaciones:",extragrande)





