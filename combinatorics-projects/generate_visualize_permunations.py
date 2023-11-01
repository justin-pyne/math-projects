import itertools
import matplotlib.pyplot as plt

# define elements
elements = ['A', 'B', 'C', 'D']

# generate perms
permutations = list(itertools.permutations(elements))

# assign color to elements
colors = {'A': 'red', 'B': 'green', 'C': 'blue', 'D': 'yellow'}


fig, axs = plt.subplots(len(permutations), 1, figsize=(2, 10))

# creating visual
for i, permutation in enumerate(permutations):
    for j, element in enumerate(permutation):
        axs[i].add_patch(plt.Rectangle((j, 0), 1, 1, color=colors[element]))
    axs[i].set_xlim(0, len(elements))
    axs[i].set_ylim(0, 1)
    axs[i].axis('off')

# display
plt.tight_layout()
plt.show()
