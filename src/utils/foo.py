from ..decorators import development, development_function


@development
class ResearchObject:
    def __init__(self):
        print('Initialized research object.')


class ProductionObject:
    def __init__(self):
        print('Initialized production object.')


@development_function
def research_function(a, b=1):
    return a + b


def production_function(a, b=1):
    return f'Sum: {a + b}'
