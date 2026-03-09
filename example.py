from pcfg.python.pcfg_class import ProductionRule, PCFG
from pcfg.python.pcfg_checker import PCFGChecker

# A
p1 = ProductionRule(tuple(["a", "b", "<A>"]), 0.5)
p2 = ProductionRule(tuple(["c", "<A>"]), 0.25)
p3 = ProductionRule(tuple(), 0.125)
p4 = ProductionRule(tuple(["b", "<B>"]), 0.125)
# B
p5 = ProductionRule(tuple(["c", "<B>", "c"]), 0.7)
p6 = ProductionRule(tuple(["a"]), 0.3)
rule_list = {"<A>": set({p1,p2,p3,p4}), "<B>": set({p5,p6})}

pcfg = PCFG("<A>", rule_list)

print(p1)

print(pcfg)

print( PCFGChecker.symbols_follow_regex(pcfg) )

print( PCFGChecker.production_probabilities_sum_to_one(pcfg) )

print( PCFGChecker.all_nonterminals_reachable(pcfg) )
