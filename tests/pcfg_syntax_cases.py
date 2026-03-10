from ..pcfg.python.pcfg_class import ProductionRule

REGEX_TEST_CASES = [
    ## (grammar, exception, msg)
    (
        {
            "starting_symbol": "<A>",
            "rules": {
                "<A>": set({ProductionRule(("a", "<A>"), 0.4), ProductionRule(("b", "<>>", "c"), 0.3), ProductionRule(("b"), 0.3)}),
                "<>>": set({ProductionRule(("b", "<>>"), 0.3), ProductionRule(("a", "c"), 0.7)})
            }
        },
        Exception,
        "Non-terminal symbol : <>> does not match the expected regular expression : <[^<>]>"
    )
]