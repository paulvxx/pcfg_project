from dataclasses import dataclass

@dataclass
class PCFG():
    """
    Class to keep track of attributes for a 
    Probablistic Context Free Grammar (PCFG):

    This class serves as an conventional representation of a PCFG.

    Attributes:
        - **non_terminals (set(string)): The set of all non-terminal symbols in the grammar.
        These are allowed to be upper-case strings, or bracketed <> labels.
        Examples: "A", "B", "<A>", "<Noun>", "<Case1>", etc..  
        - **starting_symbol (string): The value of the starting non-terminal symbol 
        in the grammar. Be sure to specify this value, otherwise, the 
        starting symbol will be selected as the first element of the 
        non-terminal symbols set upon construction.
        - **terminals (set(character)): The set of all terminal symbols in the grammar.
        These are allowed to be any set of ASCII characters 
        (except upper-case and <> characters to prevent ambiguity), 
        and can either be wrapped in quotes or quote-free.
        Only a-z is allowed without quotes (i.e. aAb), but to use special 
        characters (like [ or ], you must wrap them in quotes or 
        double quotes) i.e. '('A')'. 
        multiple characters in the same string-quote for production rules as seen 
        as concatenated (sequential) together. For example, "ab"A is intepreted as 
        terminal symbols "a" and "b" appended before non-terminal symbol A, not as one
        terminal symbol "ab".
        A Rule consist of a triple (non-terminal, production, probability): 
            - non-terminal: string
            - production : A sequence of non-terminals/terminals of arbitrary length
            - probability : a float indicating the probability this rule is chosen on
            generation / sampling.
        - **rules: (string, set( (production, probability) ))
        A dictionary with keys as non-terminal symbols and values consist of a set of
        ordered pairs dictating all possible production rules for a single non-terminal
        symbol. For example,  A --> "ab"A (0.25) | "bc"A"c" (0.75) would be stored as:
        rules["A"] = set({(("a", "b", "A"), 0.25), (("b", "c", "A", "c"), )})
        Note: All probabilities should sum to one, given some tolerance level.
        - ** epsilon : A tolerance window for determining if all production rule probabilities
        for a given non-terminal symbol sum to 1 +- epsilon. for example, if epsilon is 0.001, then
        A --> "ab"A (0.355) | "bc"A"c" (0.254) | "bb"A (0.35), then the probabilities sum to 0.999, 
        which is in the tolerable range 1 +- 0.001. 
    """
    