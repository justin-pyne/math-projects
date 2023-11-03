import plotly.graph_objects as go
import numpy as np

# sphere
phi = np.linspace(0, np.pi, 100)  # co-latitude
theta = np.linspace(0, 2 * np.pi, 100)  # longitude
phi, theta = np.meshgrid(phi, theta)
phi, theta = phi.flatten(), theta.flatten()

x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

# 2. project sphere to cube
def sphere_to_cube(x, y, z):
    max_axis = np.max([abs(x), abs(y), abs(z)])
    return x/max_axis, y/max_axis, z/max_axis

cube_x, cube_y, cube_z = np.vectorize(sphere_to_cube)(x, y, z)

# morphing and plotting
def morph_shapes(alpha, s_x, s_y, s_z, c_x, c_y, c_z):
    morphed_x = (1-alpha)*np.array(c_x) + alpha*np.array(s_x)
    morphed_y = (1-alpha)*np.array(c_y) + alpha*np.array(s_y)
    morphed_z = (1-alpha)*np.array(c_z) + alpha*np.array(s_z)
    return morphed_x, morphed_y, morphed_z

# init plot (cube)
m_x, m_y, m_z = morph_shapes(0, x, y, z, cube_x, cube_y, cube_z)
scatter = go.Scatter3d(x=m_x, y=m_y, z=m_z, mode='markers', marker=dict(size=2))

# create figure
fig = go.Figure(data=[scatter])
fig.update_layout(title='Morphing Cube to Sphere', autosize=False, 
                  width=500, height=500, margin=dict(l=65, r=50, b=65, t=90))

# slider
steps = []
for step in np.linspace(0, 1, 100):
    m_x, m_y, m_z = morph_shapes(step, x, y, z, cube_x, cube_y, cube_z)
    step_dict = {
        'args': [{'x': [m_x], 'y': [m_y], 'z': [m_z]}, [0]],
        'label': str(round(step, 2)),
        'method': 'restyle'
    }
    steps.append(step_dict)

slider = go.layout.Slider(steps=steps)
fig.update_layout(sliders=[slider])

fig.show()
