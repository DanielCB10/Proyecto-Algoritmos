def min_monedas_dinamica(denominaciones, D):
    dp = [float('inf')] * (D + 1)
    dp[0] = 0
    for i in range(1, D + 1):
        for d in denominaciones:
            if d <= i:
                dp[i] = min(dp[i], dp[i - d] + 1)
    return dp[D]

# Ejemplo de uso
