import time

def min_monedas_dinamica(denominaciones, D):
    start_time = time.time()  # Iniciar medición de tiempo
    
    dp = [float('inf')] * (D + 1)
    dp[0] = 0
    for i in range(1, D + 1):
        for d in denominaciones:
            if d <= i:
                dp[i] = min(dp[i], dp[i - d] + 1)
    
    end_time = time.time()  # Finalizar medición de tiempo
    tiempo_ejecucion = end_time - start_time
    
    return "Número de monedas:", dp[D], "Tiempo de ejecución:", tiempo_ejecucion