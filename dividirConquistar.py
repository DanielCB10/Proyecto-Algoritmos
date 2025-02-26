def min_monedas_divide_conquistar(denominaciones, D):
    if D == 0:
        return 0
    min_monedas = float('inf')
    for d in denominaciones:
        if d <= D:
            subproblema = min_monedas_divide_conquistar(denominaciones, D - d)
            if subproblema + 1 < min_monedas:
                min_monedas = subproblema + 1
    return min_monedas

