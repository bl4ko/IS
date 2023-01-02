"""Simple genetic algorithm example"""
import random


def function(x, y, z):
    """The function we are trying to optimize"""
    # We are searching for a solution (x,y,z) that solves (optimizes) 6x^3 + 9y^2 + 90z = 25
    return 6 * x**3 + 9 * y**2 + 90 * z - 25


def fitness(x, y, z):
    """Fitness function"""
    ans = function(x, y, z)

    # A way of ranking our parameters
    # If the answer is 0, we have a perfect solution
    if ans == 0:
        return 99999
    # Else sort the other solutions
    # Closer the answer is to 0, the better the fitness
    else:
        return abs(1 / ans)


# generate solutions
solutions = []
for s in range(1000):
    solutions.append(
        (random.uniform(0, 10000), random.uniform(0, 10000), random.uniform(0, 10000))
    )

# Create Genetic Algorithm
for i in range(10000):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0], s[1], s[2]), s))
    rankedsolutions.sort()
    rankedsolutions.reverse()

    print(f"=== Generation {i} best solutions ==== ")
    print(rankedsolutions[0])

    # Check if ranked solution is good enough
    if rankedsolutions[0][0] > 999:
        break

    # Combine the best solutions in our solution set, and make a new solution
    bestsolutions = rankedsolutions[:100]  # Get the top 100 solutions

    elements = []
    for s in bestsolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])

    # Create a new generation
    newGen = []
    for _ in range(1000):
        e1 = random.choice(elements) * random.uniform(
            0.99, 1.01
        )  # Mutate the solution by 2 percent
        e2 = random.choice(elements) * random.uniform(0.99, 1.01)
        e3 = random.choice(elements) * random.uniform(0.99, 1.01)

        newGen.append((e1, e2, e3))

    solutions = newGen
