from programacionDinamica import min_monedas_dinamica

denominacionesPequeño = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
DPequeño = 1234



denominacionesMediano = [1] 
for i in range(2, 200, 2):  
    denominacionesMediano.append(i)
DMediano = 10**3

denominacionesGrande = [1] 
for i in range(2, 2000, 2):  
    denominacionesGrande.append(i)
DGrande = 10**4


denominacionesExtraGrande = [1] 
for i in range(2, 20000, 2):  
    denominacionesExtraGrande.append(i)
DExtraGrande = 10**8

print(min_monedas_dinamica(denominacionesPequeño, DPequeño))
print(min_monedas_dinamica(denominacionesMediano, DMediano))
print(min_monedas_dinamica(denominacionesGrande, DGrande))
print(min_monedas_dinamica(denominacionesExtraGrande, DExtraGrande))




