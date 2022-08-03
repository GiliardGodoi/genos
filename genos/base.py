

from copy import copy

from .exceptions import HaltAlgorithm
from .condition import BaseCondition

class BaseAlgorithm:

    def __init__(self, initial_population, pipeline):

        self.initial_population = initial_population
        self.pipeline = pipeline
    
    def run(self, n):
        """
        """

        population = copy(self.initial_population)

        try:
            for age in range(n):
                BaseCondition.check(population)
                
                for step in self.pipeline:
                    population = step(population)

                population.age = age

        except HaltAlgorithm as stop:
            pass

        return population