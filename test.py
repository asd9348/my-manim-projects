import numpy as np


def dollar_val_surface(x, y):
    k = ((1 + x) / (1 + y)) - 1
    z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
    hold_val = 0.5 * (1 + x) + 0.5 * (1 + y)
    curr_val = hold_val * (1 + z)

    return np.array([ x, y, curr_val ])

# print(dollar_val_surface(-0.8, -0.99)[ 2 ])
y = -0.99

# for i in range(100):
#     print(dollar_val_surface(-0.8, y)[ 2 ])
#     y += 0.01
n=256
print([ i * 256 / n for i in range(0, n) ])
