def min_monedas_divide_conquistar(denominaciones, D, contador=[0]):
    if D == 0:
        return 0
    
    min_monedas = float('inf')
    
    for d in denominaciones:
        contador[0] += 1
        
        if d <= D:
            contador[0] += 1
            subproblema = min_monedas_divide_conquistar(denominaciones, D - d, contador)
            
            if subproblema + 1 < min_monedas:
                contador[0] += 1
                min_monedas = subproblema + 1
    
    return min_monedas
