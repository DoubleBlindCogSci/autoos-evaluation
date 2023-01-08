from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
kujc = Factor("kujc", ["lquls","squp","haggwf","lkizvu","iqqfh","ylh","rwbp"])
def jqj(kujc):
    return kujc[-2] == "rwbp" or kujc[-1] != "lkizvu"
def gvmihu(kujc):
    return not (kujc[-2] == "rwbp") and kujc[-1] == "lkizvu"
aucjnk = Factor("sqln", [DerivedLevel("nbuuf", Window(jqj, [kujc],3,1)), DerivedLevel("ladll", Window(gvmihu, [kujc],3,1))])
### EXPERIMENT
design=[kujc,aucjnk]
crossing=[aucjnk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END