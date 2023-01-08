from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
coowtg = Factor("coowtg", ["fjqhlw","xxvpye","lduno","uszqsz","ssplw","vzr"])
def qqku(coowtg):
     return coowtg[0] == "vzr" and not coowtg[-1] == "ssplw"
def auj(coowtg):
     return (not "vzr" != coowtg[0]) and  "ssplw" == coowtg[-1]
def bkfa(coowtg):
     return (coowtg[0] != "vzr") and (coowtg[-1] != "ssplw")
xzmw = DerivedLevel("amqeea", Transition(qqku, [coowtg]))
boowgv = DerivedLevel("czmiqp", Transition(auj, [coowtg]))
mktkzw = DerivedLevel("cxhs", Transition(bkfa, [coowtg]))
kdzilh = Factor("takwli", [xzmw, boowgv, mktkzw])

### EXPERIMENT
design=[coowtg,kdzilh]
crossing=[kdzilh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END