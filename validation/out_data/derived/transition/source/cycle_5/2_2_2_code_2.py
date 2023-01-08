from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jdr = Factor("jdr", ["rttsqn","wvsrp","ydo","opweim","nnfgw","dpce"])
lcg = Factor("lcg", ["rttsqn","wvsrp","ydo","opweim","nnfgw","dpce"])
jypmc = Factor("jypmc", ["rttsqn","wvsrp","ydo","opweim","nnfgw","dpce"])
def is_ntvff_hnbju(jdr, lcg, jypmc):
    return jdr[0] == jypmc[-1]
def is_ntvff_rhfw(jdr, lcg, jypmc):
    return not is_ntvff_hnbju(jdr, lcg, jypmc)
ntvff = Factor("ntvff", [DerivedLevel("hnbju", Transition(is_ntvff_hnbju, [jdr, lcg, jypmc])), DerivedLevel("rhfw", Transition(is_ntvff_rhfw, [jdr, lcg, jypmc]))])

design=[jdr,lcg,jypmc,ntvff]
crossing=[ntvff]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END