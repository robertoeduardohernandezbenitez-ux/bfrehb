from itertools import product

def sum_of_values(values,keys):
    sum=0
    n=len(values)
    for i in range(n):
        sum+=values[i]*keys[i]
    return sum

def knapsap_problem(weigth,profits,capacity, goal):
    n=len(weigth)
    sequences = product([0, 1], repeat=n)
    for sequence in sequences:
        if sum_of_values(weigth,sequence)<=capacity:
            if sum_of_values(profits,sequence)>=goal:
                return sequence
    return False