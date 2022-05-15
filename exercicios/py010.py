## Conversor de Moedas ( Cotacao Dolar e Euro do dia 06/05/2022)

dinreal = float(input(' Quanto de dinheiro você possui na carteira ? \n R$ : '))
cotacaodolar = 5.08
cotacaoeuro  = 5.36
dolar = dinreal / cotacaodolar
euro = dinreal  / cotacaoeuro

print(f' Um dolar americano é {cotacaodolar}')
print(f' Um dolar americano é {cotacaoeuro}')

print(f' Com R${dinreal:.2f} você pode comprar U${dolar:.2f}')
print(f' Com R${dinreal:.2f} você pode comprar Є${euro:.2f}')