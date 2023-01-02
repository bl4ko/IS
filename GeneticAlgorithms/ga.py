"""
Your goal is to use genetic algorithms to find a path out of any maze, represented as
 a vector of strings, where `#` characters represent walls, `.` represent empty spaces,
and S and E represent the starting and ending points, as in a given example below.
"""
import random
# maze = [
#     "####E######",
#     "##...#.####",
#     "#..#.#.####",
#     "#.##...####",
#     "#.##.#..S##",
#     "###########",
# ]
# You can move through the maze in four different directions:
# - left (`L`)
# - right (`R`)
# - up (`U`)
# - down (`D`).
# In the example above, the shortest path from the starting position `S` to the exit `E` is
# composed of the following moves: **`LLULLUUU`**.

# Task 1 - Representation
# Create a funciton that reads the 2D representation of a maze and returns the shortest path
# found by a genetic algorithm. To do this, you will need to:
# - read the map into a suitable format
# - Choose a suitable representation of your solutions (the path)
#   - Hint: you don't need to use strings when working with the genetic algorithm. You can
#     use numeric or binary representation for the GA function and then convert the result
#     to a string as the final result.
# - Define the fintess function. Make sure to penalise paths through walls - those are invalid
#   solutions.
# - Run the gentic algorithm with suitable settings.

MOVE_LIMIT = 30
POUPLATION_SIZE = 200000
MUTATION_CHANCE = 0.1
Chromosome = list[int]
Population = list[Genome]
encoding = {
    0: "L",
    1: "R",
    2: "U",
    3: "D",
}

class Player:
    def __init__(self):
        self.move_list = []
        self.fitness = 0

def generate_chromosome(length: int) -> Chromosome:
    """Generate a random genom

    Args:
        length (int): The length of the genom

    Returns:
        Genome: A random genom
    """
    return random.choices([0,1,2,3], k=length)

def generate_population(population_size: int, chromosome_length: int) -> Population:
    """Generate a random population

    Args:
        population_size (int): The size of the population
        genom_length (int): The length of the genom

    Returns:
        Population: A random population
    """
    return [generate_chromosome(chromosome_length) for _ in range(population_size)]

def is_valid_position(position: tuple[int, int], maze: list[str]) -> bool:
    """Check if a position is valid in the maze

    Args:
        position (tuple[int, int]): The position to check
        maze (list): A 2D representation of the maze

    Returns:
        bool: True if the position is valid, False otherwise
    """
    i, j = position
    if i < 0 or j < 0:
        return False
    if i >= len(maze) or j >= len(maze[0]):
        return False
    if maze[i][j] == "#":
        return False
    return True

def find_start(maze: list[str]) -> tuple[int, int]:
    """Find the starting position (S) in the maze

    Args:
        maze (list): A 2D representation of the maze

    Returns:
        tuple[int, int]: The starting position (S) in the maze
    """
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == "S":
                return (i, j)
    raise Exception("No starting position found")

def find_end(maze: list[str]) -> tuple[int, int]:
    """Find the end position (E) in the maze

    Args:
        maze (list): A 2D representation of the maze

    Returns:
        tuple[int, int]: The end position (E) in the maze
    """
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == "E":
                return (i, j)
    raise Exception("No end position found")

def is_valid_solution(solution: str, maze: list[str]) -> bool:
    """Check if a solution is valid in the maze

    Args:
        solution (str): The solution to check
        maze (list): A 2D representation of the maze

    Returns:
        bool: True if the solution is valid, False otherwise
    """
    start: tuple[int, int] = find_start(maze)
    end: tuple[int, int] = find_end(maze)
    move_dict: dict[str, tuple[int, int]] = {
        "L": (-1, 0),
        "R": (1, 0),
        "U": (0, -1),
        "D": (0, 1),
    }

    # Walk through the solution and check if we come from
    # "S" position to "E" position.
    current_pos: tuple[int, int] = start
    for i in range(1, len(solution)):
        next_pos: tuple[int, int] = current_pos + move_dict[solution[i]]
        # Check if the next position is valid
        if not is_valid_position(next_pos, maze):
            return False
        # Move to the next position
        current_pos = next_pos
    # Check if we are at the end ("E") position
    return current_pos == end

def calculate_distance(position1: tuple[int, int], position2: tuple[int, int], distance: str = "manhattan") -> int:
    """Calculate the distance between two positions

    Args:
        position1 (tuple[int, int]): The first position
        position2 (tuple[int, int]): The second position

    Returns:
        int: The distance between the two positions
    """
    match distance:
        case "euclidean":
            return ((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2) ** 0.5
        case "manhattan":
            return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])
        case _:
            raise Exception("Unknown distance")

# Read the map into a suitable format
def fitness_function(genome: Genome, end: tuple[int, int], distance: str = "manhattan") -> float:
    """Calculate the fitness of a solution

    Args:
        solution (str): The solution to check
        maze (list[str]): A 2D representation of the maze

    Returns:
        float: The fitness of the solution
    """
    if not is_valid_solution(solution, maze):
        return 0
    # Calculate the fitness (shorter the solution the better)
    return 1 / len(solution)

if __name__ == "__main__":
    # Run the genetic algorithm with suitable settings
    maze = [
        "####E######",
        "##...#.####",
        "#..#.#.####",
        "#.##...####",
        "#.##.#..S##",
        "###########",
    ]
