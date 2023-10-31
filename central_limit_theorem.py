import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def central_limit_theorem():
    np.random.seed(0)
    samples = 1000
    sample_size = 30
    means = []

    for _ in range(samples):
        data = np.random.randint(0, 100, size=sample_size)
        sample_mean = np.mean(data)
        means.append(sample_mean)

    # Plot histogram of sample means
    plt.hist(means, bins=30, density=True, color='blue', alpha=0.7)

    # Fit normal distribution to sample means and plot
    mu, std = norm.fit(means)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, label="Fit")

    title = "Central Limit Theorem\nFit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.legend()
    plt.show()

central_limit_theorem()

