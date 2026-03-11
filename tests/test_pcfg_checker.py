import pytest
import re
from ..pcfg.python.pcfg_class import ProductionRule, PCFG
from ..pcfg.python.pcfg_checker import PCFGChecker
from .pcfg_syntax_cases import INVALID_REGEX_TEST_CASES
from .pcfg_syntax_cases import VALID_REGEX_TEST_CASES
from .pcfg_syntax_cases import PROBABILITY_TEST_CASES

class TestSyntaxCases:

    @pytest.mark.parametrize("grammar, etype, msg", INVALID_REGEX_TEST_CASES)
    def test_invalid_test_cases_regex(self, grammar, etype, msg):
        """
        Verifies the symbols_follow_regex syntax checker 
        raises the appropriate Exceptions / Errors
        for invalid Grammar symbols
        """

        pcfg = PCFG(grammar["starting_symbol"], grammar["rules"])
        # Ensure we raise the appropriate exception
        print(msg)
        with pytest.raises(etype, match=re.escape(msg)):
            PCFGChecker.symbols_follow_regex(pcfg)


    @pytest.mark.parametrize("grammar", VALID_REGEX_TEST_CASES)
    def test_valid_test_cases_regex(self, grammar):
        """
        Verifies the symbols_follow_regex syntax checker 
        passes correctly for proper grammar (pcfg) specification
        """

        pcfg = PCFG(grammar["starting_symbol"], grammar["rules"])
        assert PCFGChecker.symbols_follow_regex(pcfg)


    @pytest.mark.parametrize("grammar, expected", PROBABILITY_TEST_CASES)
    def test_probability_cases(self, grammar, expected):
        """
        Verifies the symbols_follow_regex syntax checker 
        passes correctly for proper grammar (pcfg) specification
        """

        pcfg = None
        if "epsilon" in grammar:
            pcfg = PCFG(grammar["starting_symbol"], grammar["rules"], grammar["epsilon"])
        else:
            pcfg = PCFG(grammar["starting_symbol"], grammar["rules"])

        assert PCFGChecker.production_probabilities_sum_to_one(pcfg) == expected

