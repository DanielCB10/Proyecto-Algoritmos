import time

def min_monedas_divide_conquistar(denominaciones, D):
    start_time = time.time()  # Iniciar medición de tiempo
    
    if D == 0:
        return 0, 0.0
    
    min_monedas = float('inf')
    
    for d in denominaciones:
        if d <= D:
            subproblema, _ = min_monedas_divide_conquistar(denominaciones, D - d)
            if subproblema + 1 < min_monedas:
                min_monedas = subproblema + 1
    
    end_time = time.time()  # Finalizar medición de tiempo
    tiempo_ejecucion = end_time - start_time
    
    return min_monedas, tiempo_ejecucion
