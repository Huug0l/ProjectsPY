## Primeiro e último nome de uma pessoa

nome = str(input('Qual seu nome completo ? ')).strip().split()
print(f'Seu primeiro nome é {nome[0]}. \nSeu último nome é {nome[-1]}.')