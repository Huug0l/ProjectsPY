## fragmentando um numero inteiro e decimal
## quebrando um numero

## import math  - importando toda a biblioteca math
## from math import trunc - importando somente o metodo trunc da biblioteca math

from math import trunc

n1 = float(input('Digite um numero :'))
print(f'O numero {n1} tem a parte inteira {trunc(n1)}')

## transformando numero quebrado em inteiro 
## sem importar biblioteca

n2 = float(input('Digite um numero :'))
print(f'O numero {n2} tem a parte inteira {int(n1)}')