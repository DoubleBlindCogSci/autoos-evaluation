from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rrrb= Factor("rrrb", ["kmb","lfgqbm","omv","xpwek","eblyp","waem","qan"])
def is_znwasq_witl(rrrb):
    return rrrb[0] == "waem" and rrrb[-1] != "omv"
def is_znwasq_buqur(rrrb):
    return not is_znwasq_witl(rrrb)
znwasq= Factor("znwasq", [DerivedLevel("witl", Transition(is_znwasq_witl, [rrrb])), DerivedLevel("buqur", Transition(is_znwasq_buqur, [rrrb]))])

design=[rrrb,znwasq]
crossing=[znwasq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
