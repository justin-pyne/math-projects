import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def create_custom_distribution():
    # prompt user to select the type of distribution
    distribution_type = input("Enter the type of distribution (discrete/continuous): ").lower()
    
    if distribution_type == 'discrete':
        # prompt user to input outcomes and probabilities
        outcomes = input("Enter the possible outcomes separated by a space: ").split()
        probabilities = list(map(float, input("Enter the corresponding probabilities separated by a space: ").split()))
        
        # check if the # of outcomes matches # of probabilities and if probabilities sum to 1
        if len(outcomes) != len(probabilities) or abs(sum(probabilities) - 1) > 1e-6:
            print("Invalid inputs. The number of outcomes must match the number of probabilities, and the probabilities must add up to 1.")
            return
        
        # visualize the distro and calc stats
        visualize_discrete_distribution(outcomes, probabilities)
        calculate_discrete_statistics(outcomes, probabilities)
        
        # prompt user to perform operations on random variables
        perform_discrete_operations(outcomes, probabilities)
        
    elif distribution_type == 'continuous':
        # prompt user for PDF function
        pdf = input("Enter the probability density function (PDF) as a lambda function of x: ")
        pdf = eval(pdf)
        
        # prompt user for range of outcomes
        min_outcome = float(input("Enter the minimum outcome: "))
        max_outcome = float(input("Enter the maximum outcome: "))
        
        # visualize the distribution and calculate stats
        visualize_continuous_distribution(pdf, min_outcome, max_outcome)
        calculate_continuous_statistics(pdf, min_outcome, max_outcome)
        
        # prompt user to perform operations on random variables
        # perform_continuous_operations(pdf, min_outcome, max_outcome)  # to be implemented
        
    else:
        print("Invalid distribution type.")
        return
    
def add_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
    outcome_dict = {}
    
    for i, o1 in enumerate(map(float, outcomes1)):
        for j, o2 in enumerate(map(float, outcomes2)):
            outcome_sum = o1 + o2
            probability_product = probabilities1[i] * probabilities2[j]
            
            if outcome_sum in outcome_dict:
                outcome_dict[outcome_sum] += probability_product
            else:
                outcome_dict[outcome_sum] = probability_product
                
    sorted_outcomes = sorted(outcome_dict.keys())
    sorted_probabilities = [outcome_dict[o] for o in sorted_outcomes]
    
    return sorted_outcomes, sorted_probabilities

def subtract_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
    outcome_dict = {}

    for i, o1 in enumerate(map(float, outcomes1)):
        for j, o2 in enumerate(map(float, outcomes2)):
            outcome_diff = o1 - o2
            probability_product = probabilities1[i] * probabilities2[j]

            if outcome_diff in outcome_dict:
                outcome_dict[outcome_diff] += probability_product
            else:
                outcome_dict[outcome_diff] = probability_product

    sorted_outcomes = sorted(outcome_dict.keys())
    sorted_probabilities = [outcome_dict[o] for o in sorted_outcomes]

    return sorted_outcomes, sorted_probabilities


def multiply_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
    outcome_dict = {}

    for i, o1 in enumerate(map(float, outcomes1)):
        for j, o2 in enumerate(map(float, outcomes2)):
            outcome_product = o1 * o2
            probability_product = probabilities1[i] * probabilities2[j]

            if outcome_product in outcome_dict:
                outcome_dict[outcome_product] += probability_product
            else:
                outcome_dict[outcome_product] = probability_product

    sorted_outcomes = sorted(outcome_dict.keys())
    sorted_probabilities = [outcome_dict[o] for o in sorted_outcomes]

    return sorted_outcomes, sorted_probabilities


def divide_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
    outcome_dict = {}

    for i, o1 in enumerate(map(float, outcomes1)):
        for j, o2 in enumerate(map(float, outcomes2)):
            if o2 == 0:  # handle division by zero
                continue
            outcome_division = o1 / o2
            probability_product = probabilities1[i] * probabilities2[j]

            if outcome_division in outcome_dict:
                outcome_dict[outcome_division] += probability_product
            else:
                outcome_dict[outcome_division] = probability_product

    sorted_outcomes = sorted(outcome_dict.keys())
    sorted_probabilities = [outcome_dict[o] for o in sorted_outcomes]

    return sorted_outcomes, sorted_probabilities

def visualize_continuous_distribution(pdf, min_outcome, max_outcome):
    # plot the continuous probability distribution
    x = np.linspace(min_outcome, max_outcome, 1000)
    y = [pdf(xi) for xi in x]
    plt.plot(x, y)
    plt.xlabel('Outcomes')
    plt.ylabel('Probability Density')
    plt.title('Continuous Probability Distribution')
    plt.show()

def calculate_continuous_statistics(pdf, min_outcome, max_outcome):
    # calculate expected value
    expected_value, _ = quad(lambda x: x * pdf(x), min_outcome, max_outcome)
    
    # calculate variance
    variance, _ = quad(lambda x: (x - expected_value)**2 * pdf(x), min_outcome, max_outcome)
    
    # display expected value and variance
    print(f"Expected Value: {expected_value}")
    print(f"Variance: {variance}")

def visualize_discrete_distribution(outcomes, probabilities):
    # plot the custom probability distribution
    plt.bar(outcomes, probabilities)
    plt.xlabel('Outcomes')
    plt.ylabel('Probabilities')
    plt.title('Custom Probability Distribution')
    plt.show()

def calculate_discrete_statistics(outcomes, probabilities):
    # calculate expected value and variance
    expected_value = sum(o * p for o, p in zip(map(float, outcomes), probabilities))
    variance = sum(p * (o - expected_value)**2 for o, p in zip(map(float, outcomes), probabilities))
    
    # display expected value and variance
    print(f"Expected Value: {expected_value}")
    print(f"Variance: {variance}")

def perform_discrete_operations(outcomes, probabilities):
    # prompt user for another set of outcomes and probabilities for operation
    outcomes2 = input("Enter another set of possible outcomes separated by a space: ").split()
    probabilities2 = list(map(float, input("Enter the corresponding probabilities separated by a space: ").split()))

    # validate the second set of inputs
    if len(outcomes2) != len(probabilities2) or abs(sum(probabilities2) - 1) > 1e-6:
        print("Invalid inputs. The number of outcomes must match the number of probabilities, and the probabilities must add up to 1.")
        return

    # prompt user to select operation
    operation = input("Enter the operation to perform (add/subtract/multiply/divide): ").lower()

    if operation == 'add':
        # perform addition of random variables
        resulting_outcomes, resulting_probabilities = add_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    elif operation == 'subtract':
        # perform subtraction of random variables
        resulting_outcomes, resulting_probabilities = subtract_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    elif operation == 'multiply':
        # perform multiplication of random variables
        resulting_outcomes, resulting_probabilities = multiply_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    elif operation == 'divide':
        # perform division of random variables
        resulting_outcomes, resulting_probabilities = divide_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    else:
        print("Invalid operation.")
        return

    # visualize the resulting distribution after operation
    visualize_discrete_distribution(resulting_outcomes, resulting_probabilities)


# run the program
create_custom_distribution()
