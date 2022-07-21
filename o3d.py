import open3d as o3d

import numpy as np
from pprint import pprint
# print("Testing mesh in Open3D...")
# armadillo_mesh = o3d.data.ArmadilloMesh()
# mesh = o3d.io.read_triangle_mesh(armadillo_mesh.path)
# my_mesh = o3d.io.read_triangle_mesh('tetrahedron.ply')
#
#
# # 0.000000 0.000000 0.000000
# # 1.000000 0.000000 0.000000
# # 1.000000 1.000000 0.000000
# # 0.000000 1.000000 0.000000
# # 0.500000 0.500000 1.600000
# # 3 1 0 3
# # 3 1 3 2
# # 3 0 1 4
# # 3 0 4 3
# # 3 3 4 2
# # 3 1 2 4
# #
#
#
# knot_mesh = o3d.data.KnotMesh()
# mesh = o3d.io.read_triangle_mesh(knot_mesh.path)
# mesh.compute_vertex_normals()
#
# o3d.visualization.draw_geometries([mesh])
#
# print(mesh)
# print('Vertices:')
# # print(np.asarray(my_mesh.vertices))
# print(mesh.vertices)
# print('Triangles:')
# print(np.asarray(mesh.triangles))
print("Testing mesh in Open3D...")


def get_ply_file_triangles(file_name):
    mesh =o3d.io.read_triangle_mesh(file_name)
    # mesh.compute_vertex_normals()
    return np.asarray(mesh.triangles).tolist()

def get_ply_file_vertexs(file_name):
    mesh =o3d.io.read_triangle_mesh(file_name)
    # mesh.compute_vertex_normals()
    return np.asarray(mesh.vertices).tolist()

knot_mesh = o3d.data.KnotMesh()
mesh = o3d.io.read_triangle_mesh(knot_mesh.path)
# mesh =o3d.io.read_triangle_mesh('sphere.ply')

sample_pcd_data = o3d.data.PCDPointCloud()
pcd = o3d.io.read_point_cloud(sample_pcd_data.path)
o3d.io.write_point_cloud("copy_of_fragment.pcd", pcd)

print(mesh)
# print('Vertices:')
# print(np.asarray(mesh.vertices))
# print('Triangles:')
# print(np.asarray(mesh.triangles))
pprint(np.asarray(mesh.vertices).tolist())


# pprint(np.asarray(mesh.triangles).tolist())


mesh.compute_vertex_normals()
o3d.io.write_triangle_mesh("copy_of_knot.ply", mesh)

# o3d.visualization.ViewControl.scale(scale=2.5)

o3d.visualization.draw_geometries([mesh])

print(get_ply_file_vertexs(file_name))

