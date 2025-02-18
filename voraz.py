def min_monedas_voraz(denominaciones, D):
    denominaciones.sort(reverse=True)  # Asegurar que estén en orden decreciente
    num_monedas = 0
    for d in denominaciones:
        while D >= d:
            D -= d
            num_monedas += 1
    return num_monedas

# Ejemplo de uso
denominaciones = [25, 10, 5, 1]
D = 63
print("Número mínimo de monedas (Voraz):", min_monedas_voraz(denominaciones, D))

