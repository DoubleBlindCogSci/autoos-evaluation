from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
coowtg = Factor("coowtg", ["fjqhlw","xxvpye","lduno","uszqsz","ssplw","vzr"])
def is_takwli_amqeea(coowtg):
    return coowtg[0] == "vzr" and coowtg[-1] != "ssplw"
def is_takwli_czmiqp(coowtg):
    return coowtg[0] != "vzr" and coowtg[-1] == "ssplw"
def is_takwli_cxhs(coowtg):
    return not (is_takwli_amqeea(coowtg) or is_takwli_czmiqp(coowtg))
takwli = Factor("takwli", [DerivedLevel("amqeea", Transition(is_takwli_amqeea, [coowtg])), DerivedLevel("czmiqp", Transition(is_takwli_czmiqp, [coowtg])), DerivedLevel("cxhs", Transition(is_takwli_cxhs, [coowtg]))])

design=[coowtg,takwli]
crossing=[takwli]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END