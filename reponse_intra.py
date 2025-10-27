##########################################
# de Sousa-Landry, Léa, <6315829>
##########################################
import random
import numpy as np
import matplotlib.pyplot as plt

#question 1


def question1():
    #j'ai seulement été capable de générer une valeur et non 10
    temperature = random.uniform(20, 35)
    compteur = 1
    print('jour', compteur, ':',round(temperature, 1), '°C')
    compteur += 1
    if temperature < 24:
        print('trop froid')
    elif temperature > 30:
        print('trop chaud')
    else:
        print('ok')

question1()
print(' ')



#question 2


pop_initial = float(input('entrez la population initiale de bactérie: '))
population = pop_initial * (np.pi / 1.5)
print(population * 100)


#plt.figure(figsize=(5,5))
#plt.title('croissance bactérienne')
#plt.plot([0, 10], [population], '.b*')
#plt.plot([0, 10], [50000], '.r--')
#plt.xlim([0, 10])
#plt.ylim([0, 165000])
#plt.xlabel('heures')
#plt.ylabel('population')
#plt.axis('equal')
#plt.grid()
#plt.show()


