from random import *
import numpy as np
from manim import *
data = np.array([ 50, 80, 20 ])

# UL_pos = map.get_corner(UL)
# DR_pos = map.get_corner(DR)
UL_pos = [-2,2]
DR_pos = [2,-2]

x_range = [ UL_pos[ 0 ], DR_pos[ 0 ], DR_pos[ 0 ] - UL_pos[ 0 ] ]  # [min, max, len]
y_range = [ DR_pos[ 1 ], UL_pos[ 1 ], UL_pos[ 1 ] - DR_pos[ 1 ] ]


def get_pos_on_map(x_pos, y_pos, x_range, y_range):
    new_x_pos= x_range[ 2 ]*x_pos + x_range[0]
    new_y_pos= y_range[ 2 ]*y_pos + y_range[0]

    return [new_x_pos, new_y_pos]


for i in range(100):

    print(get_pos_on_map(random(),random(), x_range,y_range))

