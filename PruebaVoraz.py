from voraz import min_monedas_voraz

denominacionesPequeño = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
DPequeño = 1234



denominacionesMediano = [1] 
for i in range(2, 10000, 2):  
    denominacionesMediano.append(i)
DMediano = 10**7


denominacionesGrande = [1] 
for i in range(2, 1000000, 2):  
    denominacionesGrande.append(i)
DGrande = 10**14

print(min_monedas_voraz(denominacionesPequeño, DPequeño))
print(min_monedas_voraz(denominacionesMediano, DMediano))
print(min_monedas_voraz(denominacionesGrande, DGrande))





