import numpy as np

from custom_manim_utils.custom_functions import *

# import pandas as pd
# from colour import Color
#
# print(type(Color(hsl=(0.33, 0.9,0.1)).get_hex()))
# # def dollar_val_surface(x, y):
# #     k = ((1 + x) / (1 + y)) - 1
# #     z = (2 * np.sqrt(k + 1) / (2 + k)) - 1
# #     hold_val = 0.5 * (1 + x) + 0.5 * (1 + y)
# #     curr_val = hold_val * (1 + z)
# #
# #     return np.array([ x, y, curr_val ])
# #
# # # print(dollar_val_surface(-0.8, -0.99)[ 2 ])
# # y = -0.99
# #
# # # for i in range(100):
# # #     print(dollar_val_surface(-0.8, y)[ 2 ])
# # #     y += 0.01
# # n=256
# # print([ i * 256 / n for i in range(0, n) ])


list = [ 1, 2 ]
list2 = np.array([ 2, 2 ]) * 2

list3 = list + list2


def func(p1, p2):
    if p1 + p2 > 1:
        p2 = p2 - (p1 + p2 - 1)
    p3 = 1 - p1 - p2
    z = p1 * (1 - p1) + p2 * (1 - p2) + p3 * (1 - p3)
    return np.array([ p1, p2, z ])


def func1(p1, p2):
    if p1 + p2 > 1:
        p2 = p2 - (p1 + p2 - 1)
    p3 = 1 - p1 - p2
    z = p1 * (1 - p1) + p2 * (1 - p2) + p3 * (1 - p3)
    return [ p1, p2, z ]


i = 0
list = [ ]

from sympy import Symbol, solve, Eq, latex, simplify
import sympy as sp
from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# e1 = Eq((x+4)**(2)+(y-2)**(2)+(z-3)**(2), 4)
sphere = (x + 4) ** (2) + (y - 2) ** (2) + (z - 3) ** (2) - 4
plane = x + 4 + y - 2 + z - 3

intersect = Eq(x + 4 + y - 2 + z - 3,0)

x_val = -2
y_val = -2
z_val = 2
# print(plane.evalf(subs={x: x_val, y: y_val}))
# print(solve(plane.evalf(subs={x: x_val, y: y_val}), z))
#
# total = Eq((x + 4) ** (2) + (y - 2) ** (2) + (z - 3) ** (2) - 4, x + 4 + y - 2 + z - 3)
# print(total.evalf(subs={x: x_val, y: y_val}))
# print(solve(total.evalf(subs={x: x_val, y: y_val}), z))
# print(plane.evalf(subs={z_val:2}))
# print(solve(plane.evalf(subs={z_val:2}), z))
(x + 4) ^(2) + (y - 2) ^ (2) + (z - 3) ^ (2) - 4- x - 4 - y + 2 - z + 3
total = Eq((x + 4) ** (2) + (y - 2) ** (2) + (z - 3) ** (2) - 4, x + 4 + y - 2 + z - 3)
# print(total.evalf(subs={z_val:2}))
# print(solve(total.evalf(subs={z_val:2}), ))

# expr = (x+4)**(2)+(y-2)**(2)+(z-3)**(2)-4-x-4-y+2-z+3

# e1.ev
# print(solve(e1 ))

plane = Eq(x + 4 + y - 2 + z - 3, 0)
print(solve(plane, z))

# print(latex(solve([ e1, e2 ])))
# print(latex(solve([e1, e2])))
# print(latex(simplify(expr)))
a = -4
b = 2

print(7 / 2 - np.sqrt(-4 * a ** 2 - 28 * a - 4 * b ** 2 + 20 * b - 55) / 2)

print(np.sqrt(-4 * a ** 2 - 28 * a - 4 * b ** 2 + 20 * b - 55) / 2 + 7 / 2)

# for u in np.linspace(0., 1., 11):
#     for v in np.linspace(0., 1., 11):
#         print(func1(u, v))
#
#         list.append(func(u, v).tolist())
#
#         i +=1
#
#
# def get_slope_with_two_points(p1, p2):
#     slope = (p2[ 1 ] - p1[ 1 ]) / (p2[ 0 ] - p1[ 0 ])
#
#     return slope
#
#
# def get_y_intersect_with_two_points(p1, p2):
#     slope = (p2[ 1 ] - p1[ 1 ]) / (p2[ 0 ] - p1[ 0 ])
#
#     y_intersect = p1[ 1 ] - slope * p1[ 0 ]
#
#     return y_intersect
#
#
# p1 = [ 1, 2 ]
# p2 = [ 1, 1 ]
#
#
# def is_in_triangle(point, A, B, C, contain_border=False):
#     COM = center_of_mass([ A, B, C ])
#     if is_on_left_by_points(A, B, COM) and \
#             is_on_left_by_points(B, C, COM) and \
#             is_on_left_by_points(C, A, COM):
#         print('we need to use left func')
#         if is_on_left_by_points(A, B, point, contain_border=contain_border) and \
#                 is_on_left_by_points(B, C, point, contain_border=contain_border) and \
#                 is_on_left_by_points(C, A, point, contain_border=contain_border):
#             print('we need to use left func, it is on left therefore in triangle')
#
#             return True
#         else:
#             print('we need to use left func, it is on right therefore not in triangle')
#             return False
#     else:
#         print('we need to use right func')
#         if is_on_right_by_points(A, B, point, contain_border=contain_border) and \
#                 is_on_right_by_points(B, C, point, contain_border=contain_border) and \
#                 is_on_right_by_points(C, A, point, contain_border=contain_border):
#             print('we need to use right func, it is on right therefore in triangle')
#             return True
#         else:
#             print('we need to use right func, it is on left therefore not in triangle')
#             return False
#

# a=[1,1,0]
# b=[2,1.5,0]
# c=[1,2,0]
#
# a=[1,1,0]
# b=[2,1.5,0]
# c=[1,2,0]
#
# a = [ 1, 1, 0 ]
# b = [ 2, 1.5, 0 ]
# c = [ 1, 2, 0 ]
# point = [ 1, 1, 0 ]
# print(is_on_left_by_points(a,c,[0,0,0]))

# print(is_in_triangle(point, a, b, c, contain_border=True))

# print(get_slope_with_two_points(p1, p2))
# print(get_y_intersect_with_two_points(p1, p2))

# print('i is ', i)
# print(list)

#
# for i in range(21):
#     list.append(i)

# print(list2)
