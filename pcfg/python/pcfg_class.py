from dataclasses import dataclass, field, InitVar
from types import MappingProxyType

"""
This Python program keeps track of an Internal Representation of 
an arbitrary probablistic context free grammar using a decorator 
and basic class internal methods
(i.e. _str_, )
"""

@dataclass(frozen=True)
class ProductionRule:
    """
    Class to store a format for a single 
    production rule, consisting of the Right Hand Side (RHS)
    of the rule, and an assigned generating probability. 
    Attributes:
        - **prod_sequence (tuple[str, ...]): an arbitrary tuple/sequence of terminals and non-terminals
        - **prob (float): The assigned probability of generating the production rule. Should be between 0 and 1
    """
    prod_sequence: tuple[str, ...]
    prob: float

    def __post_init__(self):
        # disallow empty strings in production rules
        if '' in set(self.prod_sequence):
            raise Exception("Empty string \"\" is not allowed in production rules")
        # Check that the probability is non-zero but not greater than one
        if (self.prob <= 0) or (self.prob > 1):
            raise ValueError("Error: Probability of production Rule must be in the range 0 < prob <= 1.")

@dataclass(frozen=True)
class PCFG:
    """
    Class to keep track of attributes for a 
    Probablistic Context Free Grammar (PCFG):

    This class serves as an conventional representation of a PCFG.

    Attributes:
        - **starting_symbol (string): The value of the starting non-terminal symbol 
        in the grammar. Be sure to specify this value, otherwise, the 
        starting symbol will be selected as the first element of the 
        non-terminal symbols set upon construction.
        multiple characters in the same string-quote for production rules as seen 
        as concatenated (sequential) together. For example, "ab"A is intepreted as 
        terminal symbols "a" and "b" appended before non-terminal symbol A, not as one
        terminal symbol "ab".
        A Rule consist of a triple (non-terminal, production, probability): 
            - non-terminal: string
            - production : A sequence of non-terminals/terminals of arbitrary length
            - probability : a float indicating the probability this rule is chosen on
            generation / sampling.
        - **rules: dict[str, ProductionRule]
        A dictionary with keys as non-terminal symbols and values consist of a set of
        ordered pairs dictating all possible production rules for a single non-terminal
        symbol. For example,  A --> "ab"A (0.25) | "bc"A"c" (0.75) would be stored as:
        rules["A"] = set( {(("a", "b", "A"), 0.25), (("b", "c", "A", "c"), 0.75)} )
        Note: All probabilities should sum to one, given some tolerance level.
        - ** epsilon : A tolerance window for determining if all production rule probabilities
        for a given non-terminal symbol sum to 1 +- epsilon. for example, if epsilon is 0.001, then
        A --> "ab"A (0.355) | "bc"A"c" (0.254) | "bb"A (0.35), then the probabilities sum to 0.999, 
        which is in the tolerable range 1 +- 0.001. 

        Derived Attributes:
        - **non_terminals (set(string)):
        The set of all non-terminal symbols in the grammar derived from the production rule list.
        These are allowed to be upper-case strings, or bracketed <> labels.
        Examples: "A", "B", "<A>", "<Noun>", "<Case1>", etc..  
        In regular expressions, a non-terminal symbol can be:
        '<' [^>]+ '>'
        - **terminals (set(character)): The set of all terminal symbols in the grammar also derived from
        the production rule list.
        These are allowed to be any set of ASCII characters 
        (except upper-case and <> characters to prevent ambiguity), 
        In regular expressions, a terminal symbol can be:
        [^A-Z,^<>]
    """
    starting_symbol: str
    rules: dict[str, set[ProductionRule]]
    epsilon: float = 0.0001
    non_terminals: set[str] = field(init=False, repr=True)
    terminals: set[str] = field(init=False, repr=True)

    def __post_init__(self):
        # Derive the set of Non-terminals and Terminals from the Production Rules
        # Make sure the data structures are immutable
        object.__setattr__(self, 'non_terminals', frozenset(self.rules.keys()))

        # raise an error if the start symbol is not in the non_terminal set:
        if self.starting_symbol not in self.non_terminals:
            raise KeyError("Error: Starting Symbol not found in Rule dictionary.")

        # temporary set to collect all terminal symbols
        collect_terminals = set({})
        for rule_list in self.rules.values():
            for rule in rule_list:
                if not isinstance(rule, ProductionRule):
                    raise TypeError("All rules must be instances of ProductionRule.")
                for terminal in rule.prod_sequence:
                    # Determine if the symbol is a non-terminal symbol
                    # or empty string
                    if terminal not in self.non_terminals:
                        # If not, add it to the set
                        collect_terminals.add(terminal)
        
        # Make sure the terminal set is immutable
        object.__setattr__(self, 'terminals', frozenset(collect_terminals))
        # Make the dictionary "read/view only"
        object.__setattr__(self, 'rules', MappingProxyType(self.rules))
