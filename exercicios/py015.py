##aluguel de carros

dias = int(input('Digite a quantidade de dias alugados : '))
km = float(input('Digite a quantidade de km percorridos : '))
kmperc = (km * 0.15)
diaria = (dias * 60)

print(f'\nO valor da diaria é R$ : {diaria:.2f}\n')
print(f'O valor de km percorrido é R$ : {kmperc:.2f}\n')

totdiaria = (diaria + kmperc)

print(f'O valor total do aluguel é R$ : {totdiaria:.2f}\n')


