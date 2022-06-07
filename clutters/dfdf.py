from manim import *
import itertools as it
# config.frame_width = 16
# config.frame_height = 9
from hashlib import sha256

#
# def sha256_bit_string(message):
#     hexdigest = sha256(message.encode('utf-8')).hexdigest()
#     return bin(int(hexdigest, 16))[2:]
# # target = sha256_bit_string("BTC")
#
#
# rows =4
# half_rows = int(rows / 2)
#
# width= 8
# # chunks, chunk_size = len(target), len(target)//4
# # chopped_list = [ target[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
#
# chopped_list= [target[i : i + width] for i in range(0,len(target),width)]
#
#
# print(type(half_rows))
#
# # print(type(chopped_list))
# starts = chopped_list[ :half_rows-1 ]
# ends = chopped_list[ -half_rows-1: ]
# #
# starts.extend(ends)
# starts.insert(half_rows, "djfkdjfkd")
# print(starts)
#
#
# mobs = VGroup()
# for row in range(rows):
#     mobs.add(Tex(starts[row]))
#
# mobs.arrange_in_grid(1,5)



# expr = sp.cos(x) + 1


list = [1,5,3]
new_list=[float(element) for element in list]
print(new_list)