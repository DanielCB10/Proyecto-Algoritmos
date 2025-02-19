def min_monedas_voraz(denominaciones, D):
    denominaciones.sort(reverse=True)  
    num_monedas = 0
    for d in denominaciones:
        while D >= d:
            D -= d
            num_monedas += 1
    return num_monedas





    



