
class BaseCondition:
    
    conditions = set()

    def __init__(self) -> None:
        ...

    def __enter__(self):
        ...

    def __exit__(self):
        ...

    def check(self, population):
        ...