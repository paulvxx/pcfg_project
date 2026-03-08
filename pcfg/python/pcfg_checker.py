import re
from pcfg.python.pcfg_class import ProductionRule, PCFG

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
        for terminal in pcfg.terminals:
            if re.fullmatch('[^A-Z<>]', terminal) is None:
                raise Exception(f"Terminal symbol : {terminal} does not match the expected regular expression : [^A-Z<>]")
        return True

    @staticmethod
    def production_probabilities_sum_to_one(pcfg: PCFG):
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

    @staticmethod
    def all_nonterminals_reachable(pcfg: PCFG):
        """
        This static method checks that all non-terminal symbols in the 
        grammar are reachable from the starting non-terminal symbol.

        Parameters:
            - pcfg: A probablistic context-free grammar (PCFG)
        Returns:
            - True if all the PCFG's non-terminal symbols are reachable
            from the start symbol, False otherwise
        """

        # make a set to track non terminal symbols visited
        visited_non_terminals = set({})

        # make a set to track non terminal symbols that can be reached 
        # from the starting non terminal
        reachable_non_terminals = set({})
        # Add the starting symbol to the list
        reachable_non_terminals.add(pcfg.starting_symbol)

        # Create a stack structure using a list
        stack = [pcfg.starting_symbol]

        while (reachable_non_terminals != pcfg.non_terminals and len(stack) != 0):
            nt = stack.pop()
            visited_non_terminals.add(nt)
            # Make a list of non terminals to add to the stack
            non_terminals_found = set({})
            for prod_rule in pcfg.rules[nt]:
                # filter out all non terminals
                nt_symbols_for_prod = set(prod_rule.prod_sequence).intersection(pcfg.non_terminals)
                # add them to the list of non terminals found
                non_terminals_found = non_terminals_found.union(nt_symbols_for_prod)
                # also add to the list of non terminals that are reachable
                reachable_non_terminals = reachable_non_terminals.union(non_terminals_found)

            # Add the list of non_terminals to the stack,
            # but exclude already visited terminals:
            non_terminals_found = non_terminals_found.difference(visited_non_terminals)
            stack += list(non_terminals_found)
        
        # Return true if every non terminal can be reached
        return (reachable_non_terminals == pcfg.non_terminals)
