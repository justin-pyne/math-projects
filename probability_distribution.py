import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson, skew, kurtosis

def simulate_distribution():
    # User selects a probability distribution
    distribution = input("Select a distribution (normal/binomial/poisson): ").lower()

    # Take parameters for chosen distribution
    if distribution == 'normal':
        mean = float(input("Enter the mean: "))
        std_dev = float(input("Enter the standard deviation: "))
        size = int(input("Enter the sample size: "))
        sample = np.random.normal(mean, std_dev, size)
        
    elif distribution == 'binomial':
        n = int(input("Enter the number of trials: "))
        p = float(input("Enter the probability of success on each trial: "))
        size = int(input("Enter the sample size: "))
        sample = np.random.binomial(n, p, size)
        
    elif distribution == 'poisson':
        lam = float(input("Enter the average rate of value: "))
        size = int(input("Enter the sample size: "))
        sample = np.random.poisson(lam, size)
        
    else:
        print("Invalid distribution selected.")
        return

    # gen a sample using parameters and plot along with the PDF or PMF
    plt.hist(sample, bins=30, density=True, alpha=0.6, color='g')

    if distribution == 'normal':
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, std_dev)
        plt.plot(x, p, 'k', linewidth=2)
        
    elif distribution == 'binomial':
        x = np.arange(0, n+1)
        p = binom.pmf(x, n, p)
        plt.plot(x, p, 'k', linewidth=2)

    elif distribution == 'poisson':
        x = np.arange(0, int(lam) * 3)
        p = poisson.pmf(x, lam)
        plt.plot(x, p, 'k', linewidth=2)

    title = f"Fit results: {distribution.capitalize()} distribution"
    plt.title(title)
    plt.show()

    # calculating relevant stats
    print("Statistics:")
    print(f"Mean: {np.mean(sample)}")
    print(f"Variance: {np.var(sample)}")
    print(f"Skewness: {skew(sample)}")
    print(f"Kurtosis: {kurtosis(sample)}")

# testing
simulate_distribution()
