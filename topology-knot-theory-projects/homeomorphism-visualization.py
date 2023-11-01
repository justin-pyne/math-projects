import plotly.graph_objects as go
import numpy as np

# sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

sphere = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
sphere.update_layout(title='3D Sphere', autosize=False, width=500, height=500, margin=dict(l=65, r=50, b=65, t=90))

# cube vertices
x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# 12 triangles to create faces of the cube
i = [0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 1, 1]
j = [1, 2, 5, 6, 1, 5, 3, 7, 3, 7, 2, 6]
k = [2, 3, 6, 7, 5, 4, 7, 6, 7, 4, 6, 5]




cube = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, i=i, j=j, k=k, opacity=0.5)])
cube.update_layout(title='3D Cube', autosize=False, width=500, height=500, margin=dict(l=65, r=50, b=65, t=90))

# display figures
sphere.show()
cube.show()
