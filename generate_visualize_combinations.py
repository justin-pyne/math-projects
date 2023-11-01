import itertools
import matplotlib.pyplot as plt

# list of elements
elements = ['A', 'B', 'C', 'D']

# generate conbinations, take 2
combinations = list(itertools.combinations(elements, 2))

# assign a color to each element
colors = {'A': 'red', 'B': 'green', 'C': 'blue', 'D': 'yellow'}

fig, axs = plt.subplots(len(combinations), 1, figsize=(2, 10))

# visual representation
for i, combination in enumerate(combinations):
    for j, element in enumerate(combination):
        axs[i].add_patch(plt.Rectangle((j, 0), 1, 1, color=colors[element]))
    axs[i].set_xlim(0, len(elements) - 1)
    axs[i].set_ylim(0, 1)
    axs[i].axis('off')

# display to user
plt.tight_layout()
plt.show()
