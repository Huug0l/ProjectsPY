#Pintando Parede ( largura , altura e area quadrada)
larg = float(input('Largura da parede: '))
alt  = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2 # a cada dois metros quadrados de parede precisamos de um litro de tinta
print(f'Sua parede tem a dimensao de {larg:.2f} x {alt:.2f} e sua area é de {area}m².')
print(f'Para pintar esta parede você precisa de {tinta} litros de tinta')