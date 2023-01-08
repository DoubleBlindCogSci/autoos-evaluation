from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rrrb = Factor("rrrb", ["kmb","lfgqbm","omv","xpwek","eblyp","waem","qan"])
def gez(rrrb):
    return rrrb[0] == "waem" and rrrb[-1] != "omv"
def mcjj(rrrb):
    return rrrb[0] != "waem" or not (rrrb[-1] != "omv")
mdqlp = Factor("znwasq", [DerivedLevel("witl", Transition(gez, [rrrb])), DerivedLevel("buqur", Transition(mcjj, [rrrb]))])
### EXPERIMENT
design=[rrrb,mdqlp]
crossing=[mdqlp]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END