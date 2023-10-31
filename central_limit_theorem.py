import numpy as np
import matplotlib.pyplot as plt

def central_limit_theorem():
    np.random.seed(0)
    samples = 1000
    sample_size = 30
    means = []

    for _ in range(samples):
        data = np.random.randint(0, 100, size=sample_size)
        sample_mean = np.mean(data)
        means.append(sample_mean)

    plt.hist(means, bins=30, density=True, color='blue', alpha=0.7)
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.title("Central Limit Theorem")
    plt.show()

central_limit_theorem()
