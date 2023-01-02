"""
Knapsack problem:
    Given a set of items, each with a weight and a value, determine the number
    of each item to include in a collection so that the total weight is less
    than or equal to a given limit and the total value is as large as possible.
"""
from functools import partial
import random
from collections import namedtuple
from typing import Callable, Optional

Genome = list[int]
Population = list[Genome]
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
Thing = namedtuple("Thing", ["name", "value", "weight"])
PrinterFunc = Callable[[Population, int], None]

my_things = [
    Thing("Laptop", 500, 2200),
    Thing("Headphones", 150, 160),
    Thing("Coffee Mug", 60, 350),
    Thing("Notepad", 40, 333),
    Thing("Water Bottle", 30, 192),
    Thing("Mints", 5, 25),
    Thing("Socks", 10, 38),
    Thing("Tissues", 15, 80),
    Thing("Phone", 500, 200),
    Thing("Baseball Cap", 100, 70),
]


def generate_genome(length: int) -> Genome:
    """Generate a random genome"""
    return random.choices([0, 1], k=length)


def generate_population(size: int, genome_length: int) -> Population:
    """Generate a random population"""
    return [generate_genome(genome_length) for _ in range(size)]


def fitness(genome: Genome, things: list[Thing], weight_limit: int) -> int:
    """Calculate the fitness of a genome"""
    if len(genome) != len(things):
        raise ValueError("genome and things must be of the same length")

    weight = 0
    value = 0

    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0

    return value


def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    """Select two genomes from the population using fitness proportionate selection"""
    return random.choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2,
    )


def single_point_crossover(
    first_genome: Genome, second_genome: Genome
) -> tuple[Genome, Genome]:
    """Crossover two genomes at a single point and return the two new genomes"""
    if len(first_genome) != len(second_genome):
        raise ValueError("a and b must be of the same length")

    p = random.randint(1, len(first_genome) - 1)
    return (first_genome[:p] + second_genome[p:], second_genome[:p] + first_genome[p:])


def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    """Mutate a genome by flipping num bits with probability probability"""
    for _ in range(num):
        index = random.randrange(len(genome))
        genome[index] = (
            genome[index] if random.random() > probability else 1 - genome[index]
        )

    return genome


def run_evolution(
    populat_func: PopulateFunc,
    fitness_func: FitnessFunc,
    fitness_limit: int,
    selection_func: SelectionFunc = selection_pair,
    crossovoer_func: CrossoverFunc = single_point_crossover,
    mutation_func: MutationFunc = mutation,
    generation_limit: int = 100,
    printer: Optional[PrinterFunc] = None,
) -> tuple[Population, int]:

    # Generate the initial population
    population = populat_func()

    # Start the evolution (limit the number of generations)
    for i in range(generation_limit):
        # Sort the population by fitness
        population = sorted(
            population,
            key=fitness_func,
            reverse=True,
        )

        # Print the stats for this generation
        if printer is not None:
            printer(population, i, fitness_func)

        # Check if the solution is already good enough
        if fitness_func(population[0]) >= fitness_limit:
            break

        # Keep top two solutions for the next generation
        next_generation = population[:2]

        # Generate the rest of the next generation
        for _ in range(int(len(population) / 2) - 1):
            # Select two parents
            parents = selection_func(population, fitness_func)

            # Crossover the parents
            children = crossovoer_func(parents[0], parents[1])

            # Mutate the children
            children = (mutation_func(children[0]), mutation_func(children[1]))

            # Add the children to the next generation
            next_generation.extend(children)

        # Replace the current population with the next generation
        population = next_generation

    return population, i

if __name__ == '__main__':
    # Run the evolution
    population, generations = run_evolution(
        populat_func=partial(
            generate_population, size=10, genome_length=len(my_things)
        ),
        fitness_func=partial(
            fitness, things=my_things, weight_limit=3000
        ),
        fitness_limit=1350,
        generation_limit=100,
    )

    # Print the best solution
    print(f"Generation: {generations}")
    print(f"Genome: {population[0]}")
