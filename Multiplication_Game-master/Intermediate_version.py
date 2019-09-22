import threading
import _thread as thread  # we need this low-level model to use interrupt_main
import numpy as np


def finish_time(solution):
    # Raise a KeyboardInterrupt exception in the main thread.
    # A subthread can use this function to interrupt the main thread
    thread.interrupt_main()
    print(f'Time out!\nThe solution is {solution[0]}')


def exit_after(s):

    # use as decorator to exit process if function takes longer than s seconds
    def outer(fn):
        def inner(*args):
            timer = threading.Timer(s, finish_time, args=(args,))
            timer.start()
            try:
                result = fn(*args)
            finally:
                timer.cancel()
            return result

        return inner

    return outer


def load_points(name):
    f = open(name + '.txt', 'r')
    points = f.readline()
    f.close()
    return points


def save_points(name, points):
    f = open(name + '.txt', 'w')
    f.write(str(points))
    f.close()


if __name__ == '__main__':
    Finish = True

    maximo = int(input('Maxim number of the range='))
    minimo = int(input('Minim number of the range='))
    s = int(input('How many seconds do you want per question?'))
    name = str(input("What is your name?"))

    try:
        puntos_totales = int(load_points(name))
    except:
        puntos_totales = 0

    @exit_after(s)
    def countdown(correct):
        return input()

    # Game loop
    while Finish:

        is_out_of_time = False
        num1 = np.random.randint(minimo, maximo+1)
        num2 = np.random.randint(minimo, maximo+1)
        correct = num1 * num2
        puntos = len(str(correct))
        print("{} x {} = ".format(num1, num2))

        try:
            number = countdown(correct)
        except KeyboardInterrupt:
            number = (maximo * maximo) + 1
            is_out_of_time = True

        try:
            number = int(number)
        except Exception as e:
            if number == 'Finish':
                Finish = False
            else:
                print(f'No valid number. Exception ={e}')
                number = (maximo * maximo) + 1

        if number == correct and Finish:
            puntos_totales = puntos_totales + puntos
            print("Correct \nPoints = {} \nTotal points = {}".format(puntos, puntos_totales))
        elif not is_out_of_time and Finish:
            print("Incorrect \nThe correct number is = {}".format(correct))
            input("OK?")

save_points(name=name, points=puntos_totales)
