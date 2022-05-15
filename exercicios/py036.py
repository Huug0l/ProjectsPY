# Aprovando Empréstimo
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa que você quer comprar? '))
salario = float(input('Qual o seu salário? '))
tempo = float(input('Em quantos anos você pretende pagar? '))
prestação = casa/(tempo*12)
if prestação <= 0.3*salario:
    decisão = 'ACEITAR'
else:
    decisão = 'NEGAR'
print(f"""Com um salário de R$ {salario:.2f}, 
para comprar uma casa no valor de R$ {casa:.2f}
e pagar em {tempo:.0f} anos, 
será necessário uma prestação mensal de R$ {prestação:.2f}
dessa forma, nós decidimos:
{decisão} seu pedido de emprestimo!""")