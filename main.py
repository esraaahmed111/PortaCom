# Import libraries
import random
import numpy as np
import matplotlib.pyplot as plt

# Constants
Selling_Price = 249
Administrative_Cost = 400000
Advertising_Cost = 600000
total_Fixed_Cost = Advertising_Cost + Administrative_Cost

count = 10**6
mu, Sigma = 15000, 4500

direct_Cost = list()
parts_Cost = list()
Demand = list()
Profit_List = list()

# Helper functions
def random_0to1():
    return random.uniform(0, 1)

def get_c1():
    rand_prob = random_0to1()
    if 0 <= rand_prob < 0.1:
        c1 = 43
    elif 0.1 <= rand_prob < 0.3:
        c1 = 44
    elif 0.3 <= rand_prob < 0.7:
        c1 = 45
    elif 0.7 <= rand_prob < 0.9:
        c1 = 46
    else:
        c1 = 47
    return c1

def get_c2():
    c2 = random.uniform(80, 100)
    return c2

def get_x():
    x = np.random.normal(15000, 4500)
    return x

# Initialize variables for results
loss = 0
Max = 0
Min = float('inf')

# Simulate the process
for i in range(count):
    try:
        c1 = get_c1()
        direct_Cost.append(c1)
        c2 = get_c2()
        parts_Cost.append(c2)
        x = get_x()
        Demand.append(x)
        
        profit = ((Selling_Price - c1 - c2) * x) - total_Fixed_Cost
        
        # Check for profit or loss
        if profit < 0:
            loss += 1
        else:
            Profit_List.append(profit)
        
        Max = max(profit, Max)
        Min = min(profit, Min)
        
    except Exception as e:
        print(f"Error at iteration {i}: {e}")
        continue

# Display results
print(f"Maximum Profit = {Max}")
print(f"Minimum Profit = {Min}")
if Profit_List:
    print(f"Average Profit = {sum(Profit_List) / len(Profit_List)}")
else:
    print("Average Profit = 0")
print(f"Probability of Loss = {loss / count}")
print(f"Probability of Profit = {1 - (loss / count)}")

# Visualize the data
plt.hist(direct_Cost, density=True, bins=30)
plt.ylabel('Probability of c1')
plt.xlabel('Values of c1')
plt.show()

plt.hist(parts_Cost, density=True, bins=30)
plt.ylabel('Probability of c2')
plt.xlabel('Values of c2')
plt.show()

plt.hist(Demand, density=True, bins=30)
plt.ylabel('Probability of x')
plt.xlabel('Values of x')
plt.show()

plt.hist(Profit_List, density=True, bins=30)
plt.ylabel('Probability of Profit')
plt.xlabel('Values of Profit')
plt.show()
