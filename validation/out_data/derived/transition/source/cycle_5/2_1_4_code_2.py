from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mgcc = Factor("mgcc", ["ylzbn","lcxh","vkkxfc","hhdo","pkzixb"])
def is_jdznc_lepnbv(mgcc):
    return mgcc[0] == "pkzixb" or mgcc[-1] != "ylzbn"
def is_jdznc_euqff(mgcc):
    return not is_jdznc_lepnbv(mgcc)
jdznc = Factor("jdznc", [DerivedLevel("lepnbv", Transition(is_jdznc_lepnbv, [mgcc])), DerivedLevel("euqff", Transition(is_jdznc_euqff, [mgcc]))])

design=[mgcc,jdznc]
crossing=[jdznc]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END