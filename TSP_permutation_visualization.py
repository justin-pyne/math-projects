import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.spatial import distance

# generating city list
num_cities = 10
cities = {f'City {i}': (random.randint(0, 100), random.randint(0, 100)) for i in range(num_cities)}

# plotting cities on a scatter plot
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))

for city, coord in cities.items():
    axs[0].scatter(*coord, label=city)
axs[0].set_title('Cities for the Traveling Salesman Problem')
axs[0].set_xlabel('X Coordinate')
axs[0].set_ylabel('Y Coordinate')
axs[0].legend()
axs[0].grid(True)

# visualize distances in a distance matrix
city_coords = list(cities.values())
dist_matrix = distance.cdist(city_coords, city_coords, metric='euclidean')

# plotcomb distance matrix
cax = axs[1].imshow(dist_matrix, cmap='viridis')
axs[1].set_title('Distance Matrix for Cities')
axs[1].set_xlabel('Cities')
axs[1].set_ylabel('Cities')
fig.colorbar(cax, ax=axs[1], label='Distance')
axs[1].set_xticks(range(num_cities))
axs[1].set_yticks(range(num_cities))
axs[1].set_xticklabels([f'City {i}' for i in range(num_cities)], rotation=90)
axs[1].set_yticklabels([f'City {i}' for i in range(num_cities)])
axs[1].grid(False)

plt.tight_layout()

from itertools import permutations

# brute force sol using permutations
def solve_tsp_brute_force(cities, dist_matrix):
    city_indices = list(range(len(cities)))
    min_distance = float('inf')
    min_path = None
    
    for path in permutations(city_indices):
        distance = 0
        for i in range(len(path) - 1):
            distance += dist_matrix[path[i], path[i + 1]]
        distance += dist_matrix[path[-1], path[0]]  # return to the starting city
        
        if distance < min_distance:
            min_distance = distance
            min_path = path
            
    return min_distance, min_path

# solve TSP
min_distance, min_path = solve_tsp_brute_force(cities, dist_matrix)
print('Minimum Distance:', min_distance)
print('Optimal Path:', [f'City {i}' for i in min_path])
plt.show()
