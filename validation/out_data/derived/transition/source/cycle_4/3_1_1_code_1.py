from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pzapf = Factor("pzapf", ["pac","nyn","nizn","ieem","qnrl","fpmsni","zdh"])
def ymiy(pzapf):
     return pzapf[0] == "fpmsni" and not pzapf[-1] == "ieem"
def mcmcr(pzapf):
     return (pzapf[0] != "fpmsni") and  pzapf[-1] == "ieem"
def vcv(pzapf):
     return (not ymiy(pzapf)) and (not mcmcr(pzapf))
sqrxnh = Factor("qrrz", [DerivedLevel("ehmlbs", Transition(ymiy, [pzapf])), DerivedLevel("aisbii", Transition(mcmcr, [pzapf])),DerivedLevel("irhh", Transition(vcv, [pzapf]))])
### EXPERIMENT
design=[pzapf,sqrxnh]
crossing=[sqrxnh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END