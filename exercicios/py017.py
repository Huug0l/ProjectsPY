## Como calculo cateto oposto, adjacente e hipotenusa

co = float(input('Digite o comprimento do cateto oposto : '))
ca = float(input('Digite o comprimento do cateto adjacente : '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hiponetusa vai medir : {hi:.2f}')

## import math  - importando toda a biblioteca math
## from math import trunc - importando somente o metodo trunc da biblioteca math

import math

co = float(input('Digite o comprimento do cateto oposto : '))
ca = float(input('Digite o comprimento do cateto adjacente : '))
hi = math.hypot(co, ca)
print(f'A hiponetusa vai medir : {hi:.2f}')