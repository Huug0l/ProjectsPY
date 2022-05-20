# Item 1

# Crie um array numpy chamado mult3 cotendo valores de 100 a 200, de forma que a diferença entre cada elemento seja 3. 
# Em seguida, crie os array multi3_12, contendo apenas os valores do array mult3 que são divisíveis por 12.

import numpy as np

mult3 = np.arange(100,201,3) 
  
print(mult3, "\n")


#multi3_12teste = (mult3/12)

#print(multi3_12teste, "\n")

#multi3_3 = (mult3/3)

#print(multi3_3, "\n")

#multi3_4 = (mult3/4)

#print(multi3_4, "\n")

#multi3_3teste = mult3[mult3 % 3 == 0]
#multi3_4teste = mult3[mult3 % 4 == 0]


#print(multi3_3teste, "\n")
#print(multi3_4teste, "\n")


#multi3_12 = np.concatenate((multi3_3teste, multi3_4teste), axis=None)

#multi3_12 = ((mult3[mult3 % 3 == 0]) & (mult3[mult3 % 4 == 0]))

multi3_12 = ((mult3[mult3 % 3 == 0]) and (mult3[mult3 % 4 == 0]))

#multi3_12 = np.logical_and(mult3[mult3 % 3 == 0, mult3[mult3 % 4 == 0])

print(multi3_12,"\n")