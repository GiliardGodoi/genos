# Genus

Accordingly to the Cambridge online dictionary, 'genus' means a group of plants or animals closely related than a family, but less than a species. 'Genes' is related to the part of DNA that controls several aspect from the cells development. So, `genos` is somehow in the middle of this words and Gino and Geno is country song artists duo here in Brazil.

## Another meta-heuristic population based library

This library proposes a new abstraction to work with Genetic Algorithms and other meta-heuristic based on population. I have to say that I'm heavily influenced by some observations I take from the package [evol](..). Below, theses observations are described:

## Separate of concerns

In `evol` the population object holds accountable to apply the operations (crossover, mutation, the fitness function). 

## Design pattern to compose a pipeline

The Evolution class is responsible to create and keep a list of step objects. Each step object (CrossoverStep, MutationStep etc.) then will call the respective methond in the population. 


```python

# the pipeline must be made of functions or callable objects that receive a population as a parameter and return one as well
pipeline = [
    Evaluation(),
    Normalization(),
    Selection(),
    Crossover(),
    Mutation(),
]

individuals = [Individual( random_chromosome() ) for _ in range(100)]

ancestors = Population(individuals)

ga = Algorithm(ancestors, pipeline)

with Condition():
    population = ga.run(n=500)
```

The population object should contains at least the following methods:

```python

population.lowest ## return the individual with the lowest fitness

population.highest # return the individual with the highest fitness

population.sample(n=2) # return n random individuals

population.replace(old, new) # replace the old individual by a new (and modified) individual

population.sorted() # return a list of sorted individuals

population.pop() 

population.append(individual)
```
