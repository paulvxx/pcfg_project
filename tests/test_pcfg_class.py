import pytest
from ..pcfg.python.pcfg_class import ProductionRule, PCFG
from .prod_class_cases import INVALID_PROD_RULE_CASES
from .prod_class_cases import VALID_PROD_RULE_CASES
from .prod_class_cases import PCFG_CASES

class TestProductionRuleInit:

    @pytest.mark.parametrize("seq, prob, etype, msg", INVALID_PROD_RULE_CASES)
    def test_invalid_test_cases_prod_class(self, seq, prob, etype, msg):
        """
        Verifies the ProductionRule raises the appropriate Exceptions / Errors
        for invalid input
        """
        # Ensure we raise the appropriate exception
        with pytest.raises(etype, match=msg):
            ProductionRule(seq, prob)
    
    @pytest.mark.parametrize("seq, prob", VALID_PROD_RULE_CASES)
    def test_valid_test_cases_prod_class(self, seq, prob):
        """
        Verifies the ProductionRule is configured correctly with the
        correct expected attributes
        """
        prod = ProductionRule(seq, prob)
        assert prod.prod_sequence == seq
        assert prod.prob == prob

    @pytest.mark.parametrize("start_symbol, rules, expected, exception", PCFG_CASES)
    def test_pcfg_cases(self, start_symbol, rules, expected, exception):
        """
        Verifies the PCFG class is configured / raises errors correctly
        """
        # Validate normal test cases
        if exception is None:
            pcfg = PCFG(start_symbol, rules)
            assert pcfg.non_terminals == expected["non_terminals"]
            assert pcfg.terminals == expected["terminals"]
            assert pcfg.rules == rules
        # Else check for proper Exception (Key Error)
        else:
            with pytest.raises(exception["etype"], match=exception["msg"]):
                PCFG(start_symbol, rules)
        