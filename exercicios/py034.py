salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    atual = salario * 0.15
else:
    atual = salario * 0.10
print(f'O funcionário passou a ganhar R${atual:.2f}')