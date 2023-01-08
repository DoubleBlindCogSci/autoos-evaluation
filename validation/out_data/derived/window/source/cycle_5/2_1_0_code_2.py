from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kujc = Factor("kujc", ["lquls","squp","haggwf","lkizvu","iqqfh","ylh","rwbp"])
def is_sqln_nbuuf(kujc):
    return kujc[-2] == "rwbp" or kujc[-1] != "lkizvu"
def is_sqln_ladll(kujc):
    return not is_sqln_nbuuf(kujc)
sqln = Factor("sqln", [DerivedLevel("nbuuf", Window(is_sqln_nbuuf, [kujc], 3, 1)), DerivedLevel("ladll", Window(is_sqln_ladll, [kujc], 3, 1))])

design=[kujc,sqln]
crossing=[sqln]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END