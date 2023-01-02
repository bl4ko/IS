"""Represents a population of individuals."""
import random
from Individual import Individual


class Population:
    def __init__(
        self,
        population_size: int,
        genome_length: int,
        individuals: list[Individual] = [],
        generation_number: int = 1,
    ) -> None:
        self.size: int = population_size
        self.genome_length: int = genome_length
        self.individuals: list[Individual] = individuals
        self.generation_number: int = generation_number

    def initialize_population(self) -> None:
        """Initialize the population with random individuals."""
        for _ in range(self.size):
            individual: Individual = Individual(self.genome_length)
            individual.initialize_genome()
            individual.set_generation(self.generation_number)
            self.individuals.append(individual)

    def add_individuals(self, individuals: list[Individual]) -> None:
        """Add individuals to the population."""
        self.individuals.extend(individuals)
        # Add generation number to the new individuals
        for individual in individuals:
            individual.set_generation(self.generation_number)
        self.size = len(self.individuals)

    # Kills 50 % of the population
    def kill_half_population(self) -> None:
        """Kill half of the population."""
        # self.individuals = self.individuals[: self.size // 2]
        self.individuals = random.choices(
            self.individuals,
            weights=list(range(self.size, 0, -1)),
            k=self.size // 2,
        )
        self.size = len(self.individuals)
