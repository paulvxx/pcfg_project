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
            "<A>": set({(("a", "<A>"), 0.25), (("b"), 0.25), ((), 0.5)})
        },
        None, # no need for this test case
        {
            "etype": KeyError,
            "msg": "Error: Starting Symbol not found in Rule dictionary."
        }
    ),
    # Next two test cases should not raise errors
    (
        "<A>",
        {
            "<A>": set({(("a", "<A>"), 0.25), (("b"), 0.25), ((), 0.5)})
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
            "<A>": set({(("a", "a", "<B>"), 0.1), (("c", "c", "<A>"), 0.2), (("b", "c", "<A>", "a"), 0.3), ((), 0.4)}),
            "<B>": set({(("b", "<B>"), 0.6), (("b"), 0.4)})
        },
        {
            "non_terminals": set({"<A>", "<B>"}),
            "terminals": set({"a", "b", "c"}),
        },
        None
    ),
]
