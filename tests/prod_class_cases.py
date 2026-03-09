import pytest

## Python file containing test cases for the production and PCFG class

# Invalid test cases for Prod class
INVALID_PROD_RULE_CASES = [
    (tuple([""]), 0.5, Exception, "Empty string \"\" is not allowed in production rules"),
    (tuple(['']), 0.5, Exception, "Empty string \"\" is not allowed in production rules"),
    # negative probability not allowed
    (tuple(["a", "<A>", "a"]), -0.1, ValueError, "Error: Probability of production Rule must be in the range 0 < prob <= 1."), 
    # zero probability not allowed
    (tuple(["a", "b"]), 0, ValueError, "Error: Probability of production Rule must be in the range 0 < prob <= 1."), 
    # probabiltiy greater than one not allowed
    (tuple(["a", "b"]), 1.10, ValueError, "Error: Probability of production Rule must be in the range 0 < prob <= 1.") 
]

# Valud test cases for Prod class
VALID_PROD_RULE_CASES= [
    (tuple([]), 0.25),
    (tuple(["a", "<A>", "a"]), 0.5),
    (tuple(["<A>"]), 0.2)
]