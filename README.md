# Selective Imports
Examples of how to have a monolithic repository with implementations of things that should / shouldn't be imported in production.


The main script, when run, outputs the following:

```
Import error caught for ResearchObject [Unimported]: ResearchObject. ResearchObject was not imported as development flag is False.
Initialized production object.
Successfully imported <class 'src.utils.foo.ProductionObject'>: ProductionObject
Import error caught for <function research_function at 0x107232268> [Unimported]: research_function. research_function was not imported as development flag is False.
Successfully imported <function production_function at 0x10723e730>: production_function. Sum: 3
```
