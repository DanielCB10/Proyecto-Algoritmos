import time

def min_monedas_DyCMemoizacion(denominaciones, D, memo):
    start_time = time.time()  # Iniciar medición de tiempo
    
    min_monedas = float('inf')
    
    if D == 0:
        return 0, 0.0
    
    if D < 0:
        return float('inf'), 0.0
    
    if D in memo:
        return memo[D], 0.0
    
    for d in denominaciones:
        monedas, _ = min_monedas_DyCMemoizacion(denominaciones, D - d, memo)
        if monedas != float('inf'):
            min_monedas = min(min_monedas, monedas + 1)
    
    memo[D] = min_monedas
    
    end_time = time.time()  # Finalizar medición de tiempo
    tiempo_ejecucion = end_time - start_time
    
    return min_monedas, tiempo_ejecucion

