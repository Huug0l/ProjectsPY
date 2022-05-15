#Separando dígitos de um número

num = int(input('Digite um numero : '))
unid = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10 
milhar = num // 1000 % 10

print('Analisando o numero : {}'.format(num))
print('Unidade : {}'.format(unid))
print('Dezena : {}'.format(dezena))
print('Centena : {}'.format(centena))
print('Milhar : {}'.format(milhar))