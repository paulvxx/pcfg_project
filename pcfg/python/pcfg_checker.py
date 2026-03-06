import re
from pcfg_project.pcfg.python.pcfg_class import ProductionRule, PCFG

class PCFGChecker():
    """
    A static utility method class to check that a PCFG Grammar follows various
    syntax and semantic rules to ensure consistency.
    Important Note:
    The PCFG Checker class assumes that no attributes have been modified 
    (i.e. object.__setattr__) after initialization and post initialization
    If additional rules or symbols are introducts after post-init, 
    The checking functions may not work as intended.
    """

    @staticmethod
    def symbols_follow_regex(pcfg: PCFG):
        """
        This static method checks that the set of terminal
        and non-terminal symbols follow certain regex patterns,
        which also naturally ensures the two sets are disjoint (implied)
        The Regex patterns are as follows:

        Non-Terminals: '<' [^>]+ '>'
        Terminals: [^A-Z,^<>]

        Parameters:
            - pcfg: A probablistic context-free grammar (PCFG)
        Returns:
            - True if the PCFG's terminal and non-terminal symbols follow the 
            applied regex pattern
            - Raises an Exception otherwise
        """
        for non_terminal in pcfg.non_terminals:
            if re.fullmatch('<[^<>]>', non_terminal) is None:
                raise Exception(f"Non-terminal symbol : {non_terminal} does not match the expected regular expression : <[^<>]>")
        for terminal in pcfg.non_terminals:
            if re.fullmatch('[^A-Z<>]', terminal) is None:
                raise Exception(f"Terminal symbol : {terminal} does not match the expected regular expression : [^A-Z<>]")
        return True

    @staticmethod
    def symbols_follow_regex(pcfg: PCFG):
        """
        This static method checks that the sum of probabilities for the 
        set of all production rules for all non-terminal symbols sums to 1, plus or minus
        the tolerance error (epsilon).

        Parameters:
            - pcfg: A probablistic context-free grammar (PCFG)
        Returns:
            - True if the PCFG's probabilities sum to 1, False other wise
        """

        for non_terminal in pcfg.non_terminals:
            prob_sum = 0.0
            for rule in pcfg.rules[non_terminal]:
                prob_sum += rule.prob
                # already exceeded the threshold, no need to keep checking
                if prob_sum > (1 + pcfg.epsilon):
                    return False
            # Probabilities exceeing one are detected in rule-iteration, no
            # need to check again
            # Check if the sum is below one:
            if prob_sum < (1 - pcfg.epsilon):
                return False
        
        # All probability checks passed
        return True