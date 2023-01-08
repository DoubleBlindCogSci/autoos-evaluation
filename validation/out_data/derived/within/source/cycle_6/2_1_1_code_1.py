from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ehxjm = Factor("ehxjm", ["pnc","xyu","rosp","xry","cpnn","nyacx"])
def gnl(ehxjm):
    return ehxjm != "rosp"
def ivptxc(ehxjm):
    return ehxjm == "rosp"
kuql = Factor("khzc", [DerivedLevel("zdgd", WithinTrial(gnl, [ehxjm])), DerivedLevel("vcqa", WithinTrial(ivptxc, [ehxjm]))])
### EXPERIMENT
design=[ehxjm,kuql]
crossing=[kuql]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END