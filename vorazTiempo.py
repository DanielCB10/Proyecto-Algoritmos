import time

def min_monedas_voraz(denominaciones, D):
    start_time = time.time()

    denominaciones.sort(reverse=True)  
    num_monedas = 0
    for d in denominaciones:
        while D >= d:
            D -= d
            num_monedas += 1
    end_time = time.time()
    execution_time = end_time - start_time
    
    return num_monedas,execution_time
