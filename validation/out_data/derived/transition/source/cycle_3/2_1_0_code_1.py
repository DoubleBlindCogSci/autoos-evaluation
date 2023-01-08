from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
aocjcc = Factor("aocjcc", ["zorjxn","grm","dtgb","vtqfb","sbywr","cgpu"])
def kisg(aocjcc):
    return aocjcc[0] != "sbywr" and aocjcc[-1] != "cgpu"
def zfju(aocjcc):
    return not kisg(aocjcc)
lqogv = Factor("wpwnio", [DerivedLevel("klqixa", Transition(kisg, [aocjcc])), DerivedLevel("meswvx", Transition(zfju, [aocjcc]))])
### EXPERIMENT
design=[aocjcc,lqogv]
crossing=[lqogv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END