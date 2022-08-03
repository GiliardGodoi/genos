
from typing import Any, Optional

class BaseIndividual:
    
    def __init__(self, chromosome : Any, fitness : Optional[float] = None) -> None:
        
        self.__chromosome = chromosome
        self.__fitness = fitness

    @property
    def fitness(self):
        return self.__fitness
    
    @fitness.setter
    def fitness(self, value):
        self.__fitness = value

    @property
    def chromosome(self):
        return self.__chromosome

    @chromosome.setter
    def chromosome(self, value):
        self.__chromosome = value
        self.fitness = None

    @property
    def is_evaluated(self):
        return not (self.fitness == None)

class CustomIndividual(BaseIndividual):

     def __init__(self, chromosome : Any, fitness : Optional[float] = None) -> None:
        ...
