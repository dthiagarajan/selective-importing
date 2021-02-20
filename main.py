from src.utils import ResearchObject, ProductionObject, research_function, production_function


try:
    obj = ResearchObject()
except ImportError as e:
    print(f'Import error caught for {ResearchObject}: {ResearchObject.__name__}. {str(e)}')
obj = ProductionObject()
print(f'Successfully imported {ProductionObject}: {ProductionObject.__name__}')


try:
    research_function(1, b=2)
except ImportError as e:
    print(f'Import error caught for {research_function}: {research_function.__name__}. {str(e)}')
result = production_function(1, b=2)
print(f'Successfully imported {production_function}: {production_function.__name__}. {result}')
