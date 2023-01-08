from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ehxjm = Factor("ehxjm", ["pnc","xyu","rosp","xry","cpnn","nyacx"])
def is_khzc_zdgd(ehxjm):
    return ehxjm != "rosp"
def is_khzc_vcqa(ehxjm):
    return not is_khzc_zdgd(ehxjm)
khzc = Factor("khzc", [DerivedLevel("zdgd", WithinTrial(is_khzc_zdgd, [ehxjm])), DerivedLevel("vcqa", WithinTrial(is_khzc_vcqa, [ehxjm]))])

design=[ehxjm,khzc]
crossing=[khzc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END