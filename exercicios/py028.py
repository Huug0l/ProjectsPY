## Jogo da Adivinhação v.1.0

from random import choice
print('-=-'* 19)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-=-'* 19)
lista=[0,1,2,3,4,5]
escolha=choice(lista)
n1=int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
if n1 == escolha:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(escolha,n1))
print('--FIM--')