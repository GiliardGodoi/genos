import random

class Evaluate:
    
    def __init__(self, evaluation_func):

        self.evaluation_func = evaluation_func

    def __call__(self, population):

        evaluation_func = self.evaluation_func

        for individual in population:
            individual.fitness = evaluation_func(individual.chromosome)

        return population

class Mutate:
    
    def __init__(self, mutate_func, mutation_rate : float):
        self.mutate_func = mutate_func
        self.mutation_rate = mutation_rate

    def __call__(self, population):

        mutate_func = self.mutate_func
        mutation_rate = self.mutation_rate

        for individual in population:
            if (mutation_rate == 1.0) or (random.random() < mutation_rate):
                individual.chromosome = mutate_func(individual.chromosome)
            individual.fitness = None

        return population

class Crossover:
    ...

class RandomSampleSelection:

    def __init__(self, n=None, frac=1):
        self.frac = frac

    def __call__(self, population):
        ...