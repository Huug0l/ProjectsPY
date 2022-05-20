#Conversor de Bases Numéricas
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] converter para BINARIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')
else:
    print('Opcao invalida. Tente novamente.')