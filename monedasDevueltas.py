

# Definir las funciones de los algoritmos (ya las tienes, pero las incluyo para completitud)
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

def min_monedas_voraz(denominaciones, D):
    denominaciones.sort(reverse=True)
    num_monedas = 0
    for d in denominaciones:
        while D >= d:
            D -= d
            num_monedas += 1
    return num_monedas

def min_monedas_dinamica(denominaciones, D):
    dp = [float('inf')] * (D + 1)
    dp[0] = 0
    for i in range(1, D + 1):
        for d in denominaciones:
            if d <= i:
                dp[i] = min(dp[i], dp[i - d] + 1)
    return dp[D]

# Definir las denominaciones de las monedas
denominaciones = [25, 10, 5]

# Definir los valores de D que quieres probar
D_valores = [10, 20, 50, 100, 200]

# Diccionario para almacenar los resultados
monedas = {'Divide y Conquistar': [], 'Voraz': [], 'Dinámica': []}

# Ejecutar los algoritmos para cada valor de D
for D in D_valores:
    monedas['Divide y Conquistar'].append(min_monedas_divide_conquistar(denominaciones, D))
    monedas['Voraz'].append(min_monedas_voraz(denominaciones, D))
    monedas['Dinámica'].append(min_monedas_dinamica(denominaciones, D))

# Mostrar los resultados en forma de tabla
print("D\tDivide y Conquistar\tVoraz\tDinámica")
for i, D in enumerate(D_valores):
    print(f"{D}\t{monedas['Divide y Conquistar'][i]}\t\t\t{monedas['Voraz'][i]}\t\t{monedas['Dinámica'][i]}")

