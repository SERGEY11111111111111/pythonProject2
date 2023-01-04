import numpy as np

def guess_number():
    number_to_guess = np.random.randint(1, 101)
    first = 1
    last = 100

    counter = 0
    while True:
        counter += 1
        my_number = (first + last) // 2
        print(my_number)
        if my_number > number_to_guess:
            last = my_number
        elif my_number < number_to_guess:
            first = my_number
        else:
            print(counter)
            break