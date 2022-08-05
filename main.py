def quadrado_perfeito(n):
    raizQ = int(n ** 0.5)

    if raizQ ** 2 == n:
        return print(f'{n} é um quadrado perfeito')

quadrado_perfeito(100)
