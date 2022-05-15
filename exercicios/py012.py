#Calculo com porcentagem , desconto em produto

preco = float(input('Digite o valor do produto: '))
percen = float(input('Digite o valor do desconto: '))
calculo = preco *  (percen / 100)
desconto = preco * (1 - (percen / 100))

print(f'O produto que custava R$ {preco:.2f} na promocação com o desconto de {percen:.2f}% saira por R$ {desconto:.2f}')
print(f'O total de desconto dado em R$ {calculo:.2f}')