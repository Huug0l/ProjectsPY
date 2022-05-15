## Analisando Triângulo - Lados do triangulo

l1 = float(input(' Digite o tamanho em cm do primeiro segmento: '))
l2 = float(input(' Digite o tamanho em cm do segundo segmento: '))
l3 = float(input(' Digite o tamanho em cm do terceiro segmento: '))
linhas = [l1, l2, l3]
max = max(linhas)
min = min(linhas)
print(' não existe ' if max >= l1 + l2 + l3 - max else ' existe ')