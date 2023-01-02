# Genetic Algorithm Overview
Flowchart of the genetic algorithm (GA)

```txt
     ----> Initialize population    
     |              |
     |              V
     |      Fitness Calculations
     |              |
     |              V
     |      Mating Pool
     |              |
     |              V
     |       Parents Selection
     |              |
     |              V
     |      mating --> Crossover/Mutation
     |              |
     |               V
     -------offspring
```

Genetic algorithm uses a `population` of possible solutions. Each specimen in our population is called `inidivdual` has a `genome` that encodes a solution (binary encoding of the content of backpack (for example knapsack) 10001001).

Set of all current solutions at a given point during the algorithm is called the generation (generation 0 random generated solutions).

We use a `fitness function` to determine how good a certain solution is (in knapsack fitness returns the value of the backpack).
After that we use `selection` to choose the best solutions (the ones with the highest fitness) and use them to create a new generation of solutions. We use `crossover` to combine the best solutions to create new solutions. 

Then we use `mutation` to introduce some randomness in the new generation.

```txt
# crossover: 
a = 100110 0101  ---> 100110 1010
b = 001010 1010  ---> 001010 0101
# mutation: switch certain bits
a = 100110 1010  ---> 100110 1011
b = 001010 0101  ---> 001010 0100
```