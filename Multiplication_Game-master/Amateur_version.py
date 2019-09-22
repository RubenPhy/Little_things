import time
import numpy as np

print("""Let's start the game!""")

# Inputs
Finish = True
puntos_totales = 0
maximo = int(input('Maxim number of the range='))
minimo = int(input('Minim number of the range='))

# Game loop
while Finish:
    
    num1 = np.random.randint(minimo,maximo)
    num2 = np.random.randint(minimo,maximo)
    correct = num1 * num2
    seconds = time.time()
    
    print("{} x {} = ".format(num1,num2))
    number = input("")
    
    if number == 'Finish':
        Finish = False
    else:
        number = int(number)

    puntos = len(str(correct))

    if number == correct and Finish:
        print("Corect")
        if time.time()-seconds < 5:
            puntos_totales = puntos_totales + puntos
            print("Points = {} \nTotal points = {}".format(puntos,puntos_totales))
    elif Finish:
        print("Incorrect")
        print("The correct number is = {}".format(correct))

    if time.time()-seconds > 5:
        print('Time out')
