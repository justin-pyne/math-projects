# probability-projects

This repository contains a collection of Python scripts that demonstrate various probability concepts. Each script is a separate project that focuses on specific aspects of probability, such as different probability distributions, random variables, and expected values.

## Projects

1. **Probability Distributions (`probability_distributions.py`)**

   - Simulate and visualize different probability distributions, including normal, binomial, and Poisson distributions.
   - Input parameters for the selected distribution, generate a sample, and plot the sample data along with the theoretical probability density function (PDF) or probability mass function (PMF).
   - Calculate and display relevant statistics, such as mean, variance, skewness, and kurtosis.

2. **Random Variables and Expected Values (`random_variables.py`)**

   - Understand random variables and expected values by creating a probability distribution with user-defined outcomes and probabilities.
   - Visualize the distribution and calculate/display the expected value and variance.
   - Perform operations on random variables (addition, subtraction, multiplication, division) and visualize the resulting distribution.

3. **Custom Probability Distribution (`custom_probability_distribution.py`)**

   - Create and visualize custom discrete or continuous probability distributions.
   - Calculate and display expected values and variance for the created distribution.
   - Perform and visualize operations on random variables, including addition, subtraction, multiplication, and division.

4. **Law of Large Numbers (`law_of_large_numbers.py`)**

   - Demonstrate the Law of Large Numbers through simulations and visualizations.
   - Show how the average of results obtained from a large number of trials converges to the expected value.
   - Compare results for different sample sizes to illustrate the concept.

5. **Central Limit Theorem (`central_limit_theorem.py`)**

   - Demonstrate the Central Limit Theorem through simulations and visualizations.
   - Show how the distribution of sample means approximates a normal distribution, regardless of the shape of the original data distribution.
   - Include a normal distribution fit to highlight the convergence towards normality.



## Installation

You need Python installed on your machine, and the following Python packages:

```bash
pip install numpy matplotlib scipy
```

## Usage
Each script can be run independently from the command line. For example, to run the probability distributions script, use:

```bash
python probability_distributions.py
```
