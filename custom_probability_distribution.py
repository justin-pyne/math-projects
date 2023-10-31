import matplotlib.pyplot as plt

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
        visualize_distribution(outcomes, probabilities)
        calculate_statistics(outcomes, probabilities)
        
        # prompt user to perform operations on random variables
        perform_operations(outcomes, probabilities)
        
    elif distribution_type == 'continuous':
        pass
        
    else:
        print("Invalid distribution type.")
        return

def visualize_distribution(outcomes, probabilities):
    # plot the custom probability distribution
    plt.bar(outcomes, probabilities)
    plt.xlabel('Outcomes')
    plt.ylabel('Probabilities')
    plt.title('Custom Probability Distribution')
    plt.show()

def calculate_statistics(outcomes, probabilities):
    # calculate expected value and variance
    expected_value = sum(o * p for o, p in zip(map(float, outcomes), probabilities))
    variance = sum(p * (o - expected_value)**2 for o, p in zip(map(float, outcomes), probabilities))
    
    # display expected value and variance
    print(f"Expected Value: {expected_value}")
    print(f"Variance: {variance}")

def perform_operations(outcomes, probabilities):
    pass

# run the program
create_custom_distribution()
