#Calculo com porcentagem , reajuste salario

salario = float(input('Digite o salario do funcionario: '))
percen = float(input('Digite o ajuste salarial anual: '))
calculo = salario *  (percen / 100)
ajuste = salario * (1 + (percen / 100))

print(f'O salario atual é R$ {salario:.2f} com o reajuste anual de {percen:.2f}% o funcionario recebera R$ {ajuste:.2f}')
print(f'O total de ajuste dado em R$ {calculo:.2f}')