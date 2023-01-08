from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
awjcy= Factor("awjcy", ["sml","cvrrs","mkk","ymnnn","xcjv"])

def is_asxjlq_fvhc(awjcy):
    return awjcy != "cvrrs" and awjcy == "sml"
def is_asxjlq_zicnbq(awjcy):
    return not is_asxjlq_fvhc(awjcy)
asxjlq= Factor("asxjlq", [DerivedLevel("fvhc", WithinTrial(is_asxjlq_fvhc, [awjcy])), DerivedLevel("zicnbq", WithinTrial(is_asxjlq_zicnbq, [awjcy]))])


design=[awjcy,asxjlq]
crossing=[asxjlq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
