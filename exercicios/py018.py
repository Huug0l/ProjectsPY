## Seno, Cosseno e Tangente
import math

angulo = float(input('\nDigite o angulo que você deseja : '))

seno = math.sin(math.radians(angulo))
print(f'\nO angulo de {angulo} tem o seno de {seno:.2f}\n')

cosseno = math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {cosseno:.2f}\n')

tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem a tangente de {tangente:.2f}\n')

