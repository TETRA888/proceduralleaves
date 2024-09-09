import bpy
import math
import random

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
    
    return mesh_obj

def generate_maple_leaf():
    size = random.uniform(4,5) # 5 is a good size
    width = random.uniform(0.8, 1.2) # a good range is between 0.8 and 1.2
    height = random.uniform(0.8, 1.2) # a good range is between 0.8 and 1.2
    jags = random.uniform(4, 7) # a good range is between 5 and 6
    return create_maple_object(size, width, height, jags)

def generate_maple_leaf_color(current_maple_leaf):
    """
    To generate colors for the leaf, I just manually checked the colors
    I chose a first point on the rgb color wheel and then I picked another
    point.
    """
    red = random.uniform(0.26, 0.808) # Range = 0.261745 -> 0.808201
    blue = random.uniform(0.807, 0.140) # Range = 0.807581 -> 0.140042
    green = random.uniform(0.0978, 0.0395) # Range = 0.097844 -> 0.03959
    alpha = 1.0 # this is just the transparency
    color = (red, blue, green, alpha)
    
    material = bpy.data.materials.new("Maple Color")
    material.diffuse_color = color
    
    current_maple_leaf.data.materials.append(material)
    
    

def generate_maple_patch():
    square_bounds = 10
    num_leaves = 20
    for i in range(0, num_leaves):
        current_maple_leaf = generate_maple_leaf()
        locationx = random.uniform(square_bounds*(-1), square_bounds)
        locationy = random.uniform(square_bounds*(-1), square_bounds)
        current_maple_leaf.location = (locationx, locationy, 0)
        generate_maple_leaf_color(current_maple_leaf)

generate_maple_patch()