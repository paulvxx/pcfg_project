from ..pcfg.python.pcfg_class import ProductionRule

## Python file containing test cases for the production and PCFG class

# Invalid test cases for Prod class
INVALID_PROD_RULE_CASES = [
    (("",), 0.5, Exception, "Empty string \"\" is not allowed in production rules"),
    (('',), 0.5, Exception, "Empty string \"\" is not allowed in production rules"),
    # negative probability not allowed
    (("a", "<A>", "a"), -0.1, ValueError, "Error: Probability of production Rule must be in the range 0 < prob <= 1."), 
    # zero probability not allowed
    (("a", "b"), 0, ValueError, "Error: Probability of production Rule must be in the range 0 < prob <= 1."), 
    # probabiltiy greater than one not allowed
    (("a", "b"), 1.10, ValueError, "Error: Probability of production Rule must be in the range 0 < prob <= 1.") 
]

# Valid test cases for Prod class
VALID_PROD_RULE_CASES= [
    ((), 0.25),
    (("a", "<A>", "a"), 0.5),
    (("<A>",), 0.2)
]

# Test cases for PCFG class
PCFG_CASES = [
    ## (start_symbol, rules, expected, exception)

    # Test case covering start symbol not found in dictionary
    (
        "unknown",
        {
            "<A>": set({ProductionRule(("a", "<A>"), 0.25), ProductionRule(("b"), 0.25), ProductionRule((), 0.5)})
        },
        None, # no need for this test case
        {
            "etype": KeyError,
            "msg": "Error: Starting Symbol not found in Rule dictionary."
        }
    ),

    # Test case detecting Type Instance Error 
    (
        "<A>",
        {
            "<A>": set({ProductionRule(("a", "<A>"), 0.25), (("a", "<A>"), 0.25), ProductionRule(("b",), 0.25), ProductionRule((), 0.5)})
        },
        {
            "non_terminals": set({"<A>"}),
            "terminals": set({"a", "b"}),
        },
        {
            "etype": TypeError,
            "msg": "All rules must be instances of ProductionRule."           
        }
    ),

    # Next two test cases should not raise errors
    (
        "<A>",
        {
            "<A>": set({ProductionRule(("a", "<A>"), 0.25), ProductionRule(("b",), 0.25), ProductionRule((), 0.5)})
        },
        {
            "non_terminals": set({"<A>"}),
            "terminals": set({"a", "b"}),
        },
        None
    ),

    (
        "<A>",
        {
            "<A>": set({ProductionRule(("a", "a", "<B>"), 0.1), ProductionRule(("c", "c", "<A>"), 0.2), 
                        ProductionRule(("b", "c", "<A>", "a"), 0.3), ProductionRule((), 0.4)}),
            "<B>": set({ProductionRule(("b", "<B>"), 0.4), ProductionRule(("b",), 0.3), ProductionRule(("c", "<C>", "c"), 0.3)}),
            "<C>": set({ProductionRule(("a", "d", "<A>"), 0.8), ProductionRule((), 0.2)})
        },
        {
            "non_terminals": set({"<A>", "<B>", "<C>"}),
            "terminals": set({"a", "b", "c", "d"}),
        },
        None
    ),
]
