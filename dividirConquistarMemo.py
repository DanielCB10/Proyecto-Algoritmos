def min_monedas_DyCMemoizacion(denominaciones, D, memo, operaciones):
    min_monedas = float('inf')
    operaciones[0] += 1
    if D == 0:
        return 0
    if D < 0:
        return float('inf')
    if D in memo:
        return memo[D]
    for d in denominaciones:
        monedas = min_monedas_DyCMemoizacion(denominaciones, D - d, memo, operaciones)
        if monedas != float('inf'):
            min_monedas = min(min_monedas, monedas + 1)
    memo[D] = min_monedas
    return min_monedas