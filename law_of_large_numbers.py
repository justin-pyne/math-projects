import numpy as np
import matplotlib.pyplot as plt

def law_of_large_numbers():
    np.random.seed(0)
    flips = 1000
    results = np.random.choice([0, 1], size=flips)
    running_average = np.cumsum(results) / (np.arange(flips) + 1)
    expected_value = 0.5

    plt.plot(running_average, label="Running Average")
    plt.axhline(y=expected_value, color='r', linestyle='--', label="Expected Value")
    plt.xlabel("Number of Trials")
    plt.ylabel("Average Outcome")
    plt.title("Law of Large Numbers")
    plt.legend()
    plt.show()

law_of_large_numbers()
