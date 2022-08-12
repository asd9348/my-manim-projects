import numpy as np

# nxm의 사각형이라면 일단 5x3이라고 하고
#
# array = [ ]
# for u in np.linspace(0, 2, 5):
#     row = []
#     for v in np.linspace(0, 2, 5):
#         row.append([ u, v, 0 ])
#     array.append(row)
#
# print(type(array))
# print(np.array(array))
# print(type(np.array(array)))
#
point_list = np.array(
    [ [ [ 0, 0 ,0], [ 1, 0 ,0 ] ],
      [ [ 0, 1 ,0 ], [ 1, 1 ,0 ] ]]
)

point_list+1

print(point_list+1)

map
#
# print(point_list.shape)
#
#
# n=point_list.shape[ 1 ]
# m=point_list.shape[ 0 ]
#
# print(point_list[0,0])

#n cols
#m rows
# for row in range(0,m):
#     for col in range(0,n):
#         point_list[row,col]
#
#         sqDL=point_list[row,col]
#         sqDR=point_list[row,col+1]
#         sqUR=point_list[row+1,col+1]
#         sqUL=point_list[row+1,col]
#

        # point.append(point_list[ row, col ])

# print(point)
# face.set_points_as_corners(
#     [
#         [ u1, v1, 0 ],
#         [ u2, v1, 0 ],
#         [ u2, v2, 0 ],
#         [ u1, v2, 0 ],
#         [ u1, v1, 0 ],
#     ],
# )
