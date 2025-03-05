from programacionDinamica import min_monedas_dinamica

denominacionesPequeño = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
DPequeño = 24599

denominacionesMediano = [1] 
for i in range(2, 200, 2):  
    denominacionesMediano.append(i)
DMediano = 359503

denominacionesGrande = [1] 
for i in range(2, 2000, 2):  
    denominacionesGrande.append(i)
DGrande = 9380353292

denominacionesExtraGrande = [1] 
for i in range(2, 1000000, 2):  
    denominacionesGrande.append(i)
DExtraGrande = 10**14   

print(min_monedas_dinamica(denominacionesPequeño, DPequeño))
print(min_monedas_dinamica(denominacionesMediano, DMediano))
print(min_monedas_dinamica(denominacionesGrande, DGrande))




