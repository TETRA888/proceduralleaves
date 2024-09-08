import bpy
import math

def maple_coords(t, size, width, height, jags):
    x = size * math.sin(t) * (width + 0.2 * math.cos(jags * t))
    y = size * math.cos(t) * (height + 0.2 * math.cos(jags * t))
    
    return x , y , 0 # Return x and y and 0 for the Z axis since I just want it to be flat

def create_maple_object(size, width, height, jags):
    # So now we want to create a mesh using the internal Blender-Python commands
    verts = []
    edges = []
    faces = []

    # This is just level of detail
    LOD = 20

    for i in range(1, LOD):
        verts.append(maple_coords(i * (2 * math.pi / LOD), size, width, height, jags))
        
    for i in range(0, (LOD - 1)):
        edges.append([i, (i + 1) % (LOD -1)])
        
    faces.append(list(range(LOD - 1)))

    # This is creating the mesh data to make the leave
    mesh_data = bpy.data.meshes.new("Maple Mesh Data")
    mesh_data.from_pydata(verts, edges, faces)

    # This is creating the mesh object using the mesh data
    mesh_obj = bpy.data.objects.new("Maple Object", mesh_data)

    # Here we are simply just adding the leaf to the main scene collection so we can see it
    bpy.context.collection.objects.link(mesh_obj)

size = 5 # 5 is a good size
width = 1 # a good range is between 0.8 and 1.2
height = 1 # a good range is between 0.8 and 1.2
jags = 5 # a good range is between 5 and 6
create_maple_object(size, width, height, jags)

current_maple_leaf = bpy.context.active_object


# This is just for checking the coordinates
"""
for i in range(1, 10):
    print(maple_coords(i))
"""