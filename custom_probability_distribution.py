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
        
        # check for duplicate outcomes
        if len(outcomes) != len(set(outcomes)):
            print("Invalid inputs. Outcomes must be unique.")
            return

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

        # check if the PDF is normalized
        integral, _ = quad(pdf, min_outcome, max_outcome)
        if abs(integral - 1) > 1e-6:
            print("Invalid inputs. The PDF must be normalized, i.e., the integral of the PDF over the range of outcomes must equal 1.")
            return
                
        # visualize the distribution and calculate stats
        visualize_continuous_distribution(pdf, min_outcome, max_outcome)
        calculate_continuous_statistics(pdf, min_outcome, max_outcome)
        
        # prompt user to perform operations on random variables
        perform_continuous_operations(pdf, min_outcome, max_outcome)
        
    else:
        print("Invalid distribution type.")
        return
    
def add_discrete_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
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

def subtract_discrete_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
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


def multiply_discrete_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
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


def divide_discrete_random_variables(outcomes1, probabilities1, outcomes2, probabilities2):
    outcome_dict = {}

    # Check for division by zero in outcomes2
    if 0 in map(float, outcomes2):
        print("Invalid inputs. Division by zero is not allowed.")
        return None, None

    for i, o1 in enumerate(map(float, outcomes1)):
        for j, o2 in enumerate(map(float, outcomes2)):
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
        resulting_outcomes, resulting_probabilities = add_discrete_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    elif operation == 'subtract':
        # perform subtraction of random variables
        resulting_outcomes, resulting_probabilities = subtract_discrete_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    elif operation == 'multiply':
        # perform multiplication of random variables
        resulting_outcomes, resulting_probabilities = multiply_discrete_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    elif operation == 'divide':
        # perform division of random variables
        resulting_outcomes, resulting_probabilities = divide_discrete_random_variables(outcomes, probabilities, outcomes2, probabilities2)
    else:
        print("Invalid operation.")
        return

    # visualize the resulting distribution after operation
    visualize_discrete_distribution(resulting_outcomes, resulting_probabilities)

def add_continuous_random_variables(pdf1, min_outcome1, max_outcome1, pdf2, min_outcome2, max_outcome2):
    min_sum = min_outcome1 + min_outcome2
    max_sum = max_outcome1 + max_outcome2
    
    def pdf_sum(x):
        return quad(lambda y: pdf1(y) * pdf2(x - y), min_outcome2, max_outcome2)[0]
    
    return pdf_sum, min_sum, max_sum


def subtract_continuous_random_variables(pdf1, min_outcome1, max_outcome1, pdf2, min_outcome2, max_outcome2):
    min_diff = min_outcome1 - max_outcome2
    max_diff = max_outcome1 - min_outcome2
    
    def pdf_diff(x):
        return quad(lambda y: pdf1(y) * pdf2(y - x), min_outcome2, max_outcome2)[0]
    
    return pdf_diff, min_diff, max_diff


def multiply_continuous_random_variables(pdf1, min_outcome1, max_outcome1, pdf2, min_outcome2, max_outcome2):
    min_product = min(min_outcome1 * min_outcome2, min_outcome1 * max_outcome2, max_outcome1 * min_outcome2, max_outcome1 * max_outcome2)
    max_product = max(min_outcome1 * min_outcome2, min_outcome1 * max_outcome2, max_outcome1 * min_outcome2, max_outcome1 * max_outcome2)
    
    def pdf_product(x):
        if x == 0:
            return 0
        return quad(lambda y: pdf1(y) * pdf2(x / y) / abs(y), min_outcome2, max_outcome2)[0]
    
    return pdf_product, min_product, max_product


def divide_continuous_random_variables(pdf1, min_outcome1, max_outcome1, pdf2, min_outcome2, max_outcome2):
    if min_outcome2 <= 0 <= max_outcome2:
        print("Division by zero is not allowed.")
        return None
    
    min_quotient = min(min_outcome1 / min_outcome2, min_outcome1 / max_outcome2, max_outcome1 / min_outcome2, max_outcome1 / max_outcome2)
    max_quotient = max(min_outcome1 / min_outcome2, min_outcome1 / max_outcome2, max_outcome1 / min_outcome2, max_outcome1 / max_outcome2)
    
    def pdf_quotient(x):
        return quad(lambda y: pdf1(y) * pdf2(y / x) * abs(y), min_outcome2, max_outcome2)[0]
    
    return pdf_quotient, min_quotient, max_quotient


def perform_continuous_operations(pdf, min_outcome, max_outcome):
    # prompt user for another PDF and range of outcomes for operation
    pdf2 = input("Enter another probability density function (PDF) as a lambda function of x: ")
    pdf2 = eval(pdf2)
    min_outcome2 = float(input("Enter the minimum outcome for the second PDF: "))
    max_outcome2 = float(input("Enter the maximum outcome for the second PDF: "))
    
    # check if the second PDF is normalized
    integral, _ = quad(pdf2, min_outcome2, max_outcome2)
    if abs(integral - 1) > 1e-6:
        print("Invalid inputs. The second PDF must be normalized, i.e., the integral of the PDF over the range of outcomes must equal 1.")
        return
    
    # prompt user to select operation
    operation = input("Enter the operation to perform (add/subtract/multiply/divide): ").lower()

    if operation == 'add':
        # perform addition of random variables
        resulting_pdf, min_result, max_result = add_continuous_random_variables(pdf, min_outcome, max_outcome, pdf2, min_outcome2, max_outcome2)
    elif operation == 'subtract':
        # perform subtraction of random variables
        resulting_pdf, min_result, max_result = subtract_continuous_random_variables(pdf, min_outcome, max_outcome, pdf2, min_outcome2, max_outcome2)
    elif operation == 'multiply':
        # perform multiplication of random variables
        resulting_pdf, min_result, max_result = multiply_continuous_random_variables(pdf, min_outcome, max_outcome, pdf2, min_outcome2, max_outcome2)
    elif operation == 'divide':
        # perform division of random variables
        resulting_pdf, min_result, max_result = divide_continuous_random_variables(pdf, min_outcome, max_outcome, pdf2, min_outcome2, max_outcome2)
        if resulting_pdf is None:
            return
    else:
        print("Invalid operation.")
        return
    
    # visualize the resulting distribution after operation
    visualize_continuous_distribution(resulting_pdf, min_result, max_result)
    # calculate stats for the resulting distribution
    calculate_continuous_statistics(resulting_pdf, min_result, max_result)

# # TEST CASES (uncomment and comment out the run the program call to test)
# # Test Case 1: Create and visualize discrete distribution
# def test_discrete_distribution():
#     outcomes = ['1', '2', '3', '4', '5']
#     probabilities = [0.1, 0.2, 0.3, 0.2, 0.2]
#     visualize_discrete_distribution(outcomes, probabilities)
#     calculate_discrete_statistics(outcomes, probabilities)

# # Test Case 2: Create and visualize continuous distribution
# def test_continuous_distribution():
#     def pdf(x):
#         return 1/3 if 0 <= x <= 3 else 0
#     min_outcome = 0
#     max_outcome = 3
#     visualize_continuous_distribution(pdf, min_outcome, max_outcome)
#     calculate_continuous_statistics(pdf, min_outcome, max_outcome)

# # Test Case 3: Add two discrete random variables
# def test_add_discrete_random_variables():
#     outcomes1 = ['1', '2']
#     probabilities1 = [0.5, 0.5]
#     outcomes2 = ['3', '4']
#     probabilities2 = [0.3, 0.7]
#     resulting_outcomes, resulting_probabilities = add_discrete_random_variables(outcomes1, probabilities1, outcomes2, probabilities2)
#     visualize_discrete_distribution(resulting_outcomes, resulting_probabilities)

# # Test Case 4: Add two continuous random variables
# def test_add_continuous_random_variables():
#     def pdf1(x):
#         return 1 if 0 <= x <= 1 else 0
#     min_outcome1 = 0
#     max_outcome1 = 1
    
#     def pdf2(x):
#         return 1 if 1 <= x <= 2 else 0
#     min_outcome2 = 1
#     max_outcome2 = 2
    
#     resulting_pdf, min_result, max_result = add_continuous_random_variables(pdf1, min_outcome1, max_outcome1, pdf2, min_outcome2, max_outcome2)
#     visualize_continuous_distribution(resulting_pdf, min_result, max_result)
#     calculate_continuous_statistics(resulting_pdf, min_result, max_result)

# # Run test cases
# test_discrete_distribution()
# test_continuous_distribution()
# test_add_discrete_random_variables()
# test_add_continuous_random_variables()



# run the program
create_custom_distribution()
