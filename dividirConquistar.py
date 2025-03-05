def min_monedas_divide_conquistar(denominaciones, D, contador=[0]):
    if D == 0:
<<<<<<< HEAD
        return 0, contador[0]
=======
        return 0
>>>>>>> d6263cb6b1555a179da7e09ba3ed5e5ccfb122d7
    
    min_monedas = float('inf')
    
    for d in denominaciones:
        contador[0] += 1
        
        if d <= D:
            contador[0] += 1
<<<<<<< HEAD
            subproblema, _ = min_monedas_divide_conquistar(denominaciones, D - d, contador)
=======
            subproblema = min_monedas_divide_conquistar(denominaciones, D - d, contador)
>>>>>>> d6263cb6b1555a179da7e09ba3ed5e5ccfb122d7
            
            if subproblema + 1 < min_monedas:
                contador[0] += 1
                min_monedas = subproblema + 1
    
<<<<<<< HEAD
    return min_monedas, contador[0]
=======
    return min_monedas
>>>>>>> d6263cb6b1555a179da7e09ba3ed5e5ccfb122d7
