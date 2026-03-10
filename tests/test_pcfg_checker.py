import pytest
import re
from ..pcfg.python.pcfg_class import ProductionRule, PCFG
from ..pcfg.python.pcfg_checker import PCFGChecker
from .pcfg_syntax_cases import REGEX_TEST_CASES

class TestSyntaxCases:

    @pytest.mark.parametrize("grammar, etype, msg", REGEX_TEST_CASES)
    def test_invalid_test_cases_regex(self, grammar, etype, msg):
        """
        Verifies the symbols_follow_regex syntax checker 
        raises the appropriate Exceptions / Errors
        for invalid Grammar symbols
        """

        pcfg = PCFG(grammar["starting_symbol"], grammar["rules"])
        # Ensure we raise the appropriate exception
        with pytest.raises(etype, match=re.escape(msg)):
            PCFGChecker.symbols_follow_regex(pcfg)
