from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
nygysm = Factor("nygysm", ["migfje","uiq","hgzien","gvi","jsm","suwlo"])
def yyulds(nygysm):
    return nygysm[0] == "suwlo" or nygysm[-1] != "hgzien"
def kggr(nygysm):
    return nygysm[0] != "suwlo" and nygysm[-1] == "hgzien"
gqcck = Factor("npxjy", [DerivedLevel("cuqrj", Transition(yyulds, [nygysm])), DerivedLevel("xnb", Transition(kggr, [nygysm]))])
### EXPERIMENT
design=[nygysm,gqcck]
crossing=[gqcck]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END