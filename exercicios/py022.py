#Analisador de Textos

nome = str(input('Digite seu nome completo: ')).strip()
espaco = nome.count(' ')
priespaco = nome.find(' ')
separa = nome.split()

print('Analisando seu nome ....')
print(f'Seu nome em maiusculas é : {nome.upper()}')
print(f'Seu nome em minusculas é : {nome.lower()}')
print(f'Seu nome tem {len(nome) - espaco} letras')
print(f'Seu primeiro nome tem {priespaco}')
print(f'Seu primeiro nome é {separa[0]}')