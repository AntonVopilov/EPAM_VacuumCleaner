import body
from random import randint

def hurdle_fabric(max_x, max_y, max_size, num_hardles):
    hardles = []
    for i in range(num_hardles):
        x_pos = randint(max_size, max_x - max_size)
        y_pos = randint(max_size, max_y - max_size)
        width = randint(2, max_size)
        lenght = randint(2, max_size)
        hardles.append(body.Body(x_pos, y_pos, width, lenght))
    return hardles