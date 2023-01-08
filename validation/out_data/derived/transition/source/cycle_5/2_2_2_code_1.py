from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jdr = Factor("jdr", ["rttsqn","wvsrp","ydo","opweim","nnfgw","dpce"])
lcg = Factor("lcg", ["rttsqn","wvsrp","ydo","opweim","nnfgw","dpce"])
jypmc = Factor("jypmc", ["rttsqn","wvsrp","ydo","opweim","nnfgw","dpce"])
def xpju(jdr, jypmc, lcg):
    return jdr[0] == jypmc[-1]
def lrg(jdr, jypmc, lcg):
    return not (jdr[0] == jypmc[-1])
jpm = Factor("ntvff", [DerivedLevel("hnbju", Transition(xpju, [jdr, lcg, jypmc])), DerivedLevel("rhfw", Transition(lrg, [jdr, lcg, jypmc]))])
### EXPERIMENT
design=[jdr,lcg,jypmc,jpm]
crossing=[jpm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END