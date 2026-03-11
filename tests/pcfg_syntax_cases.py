from ..pcfg.python.pcfg_class import ProductionRule

REGEX_TEST_CASES = [
    ## (grammar, exception, msg)

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
        "Non-terminal symbol : <B>C> does not match the expected regular expression : <[^<>]>"
    ),
    # NON-ACCEPTING CASES (TERMINALS)
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
    )

    # ACCEPTING CASES

]