from ..pcfg.python.pcfg_class import ProductionRule

INVALID_REGEX_TEST_CASES = [
    ## Parameters: (grammar, exception, msg)

    # NON-ACCEPTING CASES (NON-TERMINALS)
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>": set({ProductionRule(("a", "<A>"), 0.4), ProductionRule(("b", "<>>", "c"), 0.3), ProductionRule(("b",), 0.3)}),
                "<>>": set({ProductionRule(("b", "<>>"), 0.3), ProductionRule(("a", "c"), 0.7)})
            }
        },
        Exception,
        "Non-terminal symbol : <>> does not match the expected regular expression : <[^<>]>"
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>": set({ProductionRule(("a", "<A>"), 0.4), ProductionRule(("b", "<Sym>>", "c"), 0.6)}),
                "<Sym>>": set({ProductionRule(("a", "b", "c"), 0.3), ProductionRule((), 0.7)})
            }
        },
        Exception,
        "Non-terminal symbol : <Sym>> does not match the expected regular expression : <[^<>]>"
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>": set({ProductionRule(("a", "b", "<A>"), 0.1), ProductionRule(("b", "<B>C>"), 0.1), ProductionRule(("c",), 0.8)}),
                "<B>C>": set({ProductionRule(("b", "b", "<B>C>"), 0.5), ProductionRule((), 0.5)})
            }
        },
        Exception,
        "Non-terminal symbol : <B>C> does not match the expected regular expression : <[^<>]>"
    ),
    (
        {
            "starting_symbol": "",
            "rules": {
                "": set({ProductionRule(("a", "<A>"), 0.6), ProductionRule(("b", "b"), 0.4)}),
                "<A>": set({ProductionRule(("c", "b", "a"), 0.5), ProductionRule(("c",), 0.5)})
            }
        },
        Exception,
        "Non-terminal symbol :  does not match the expected regular expression : <[^<>]>"
    ),
    # NON-ACCEPTING CASES (TERMINALS)

    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("c", "<A>"), 0.3),  ProductionRule(("c",), 0.4), ProductionRule(("d", "A"), 0.3)})
            }
        },
        Exception,
        "Terminal symbol : A does not match the expected regular expression : [^A-Z<>]"
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("c", "<A>", "c"), 0.1),  ProductionRule(("<A>", "b", "b"), 0.3), ProductionRule(("<B>", "C"), 0.6)}),
                "<B>":set({ProductionRule(("c", "d"), 0.3),  ProductionRule(("a", "a"), 0.4), ProductionRule(("d", "<B>"), 0.3)})
            }
        },
        Exception,
        "Terminal symbol : C does not match the expected regular expression : [^A-Z<>]"
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("a", "b"), 0.4), ProductionRule(("<B>",), 0.6)}),
                "<B>":set({ProductionRule(("bad", "d"), 0.3),  ProductionRule(("a", "b", "<A>"), 0.3), ProductionRule((), 0.4)})
            }
        },
        Exception,
        "Terminal symbol : bad does not match the expected regular expression : [^A-Z<>]"
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("a", "<A>"), 0.4), ProductionRule(("a", "<B>"), 0.5), ProductionRule(("a", "<C>"), 0.1)}),
                "<B>":set({ProductionRule(("c", "d", "<B>", "d"), 0.6), ProductionRule(("c", "c"), 0.4)})
            }
        },
        Exception,
        "Terminal symbol : <C> does not match the expected regular expression : [^A-Z<>]"
    ),
]

VALID_REGEX_TEST_CASES = [
    ### Parameters: (grammar)

    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("a", "<A>"), 0.4), ProductionRule(("b", "<B>"), 0.2), ProductionRule(("c"), 0.4)}),
                "<B>":set({ProductionRule(("c", "c", "<B>"), 0.6), ProductionRule(("d", "<A>"), 0.1), ProductionRule((), 0.3)})
            }
        }
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("a", "a", "<B>"), 0.1), ProductionRule(("b"), 0.6), ProductionRule(("c"), 0.3)}),
                "<B>":set({ProductionRule(("a", "<B>"), 0.7), ProductionRule(("d", "<C>"), 0.3)}),
                "<C>":set({ProductionRule(("c", "<C>"), 0.25), ProductionRule(("b", "<A>"), 0.75)})
            }
        }
    )
]

PROBABILITY_TEST_CASES = [
    ### Parameters: (grammar, expected)

    # ACCEPTING CASES

    # No-Epsilon Cases
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("a", "<B>"), 0.2), ProductionRule(("a", "<A>", "b"), 0.1), ProductionRule(("a", "b"), 0.7)}),
                "<B>":set({ProductionRule(("a",), 0.3), ProductionRule(("c", "<B>"), 0.5), ProductionRule(("<A>", "b"), 0.2)}),
            },
        },
        True
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("<B>",), 0.17), ProductionRule(("<B>", "b"), 0.83)}),
                "<B>":set({ProductionRule(("<C>"), 0.21), ProductionRule(("c", "<B>"), 0.435), ProductionRule(("<A>", "a"), 0.355)}),
                "<C>":set({ProductionRule(("a", "b"), 1.0)}),
            },
        },
        True
    ),
    
    # Epsilon Cases
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("<A>", "b"), 0.49995), ProductionRule(("b"), 0.5)}),
            },
        },
        True
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("<A>", "b"), 0.2), ProductionRule(("b"), 0.80005)}),
            },
        },
        True
    ),

    # Changed Epsilon Case
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("<A>", "b"), 0.9), ProductionRule(("b"), 0.15)}),
            },
            "epsilon": 0.1
        },
        True
    ),

    # NON-ACCEPTING CASES

    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("<A>", "b"), 0.9), ProductionRule(("b"), 0.20005)}),
            },
            "epsilon": 0.1
        },
        False
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>": set({ProductionRule(("a", "<A>"), 0.4), ProductionRule(("b",), 0.4)})
            }
        },
        False
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>":set({ProductionRule(("d", "<B>"), 0.3), ProductionRule(("<B>", "b"), 0.7)}),
                "<B>":set({ProductionRule(("<C>"), 0.3), ProductionRule(("a", "<B>"), 0.5), ProductionRule(("<A>", "c"), 0.2)}),
                "<C>":set({ProductionRule(("a", "b"), 0.3), ProductionRule(("c", "d"), 0.5)}),
            },
        },
        False
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>": set({ProductionRule(("a", "<A>"), 0.6), ProductionRule(("c", "c"), 0.3), ProductionRule(("b",), 0.5)})
            }
        },
        False
    ),
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>": set({ProductionRule(("a", "<A>"), 0.1), ProductionRule(("b", "<B>"), 0.7), ProductionRule(("c",), 0.2)}),
                "<B>": set({ProductionRule(("b", "c", "<A>"), 0.5), ProductionRule((), 0.49)})
            }
        },
        False
    ),

]