from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pzapf = Factor("pzapf", ["pac","nyn","nizn","ieem","qnrl","fpmsni","zdh"])
def is_qrrz_ehmlbs(pzapf):
    return pzapf[0] == "fpmsni" and pzapf[-1] != "ieem"
def is_qrrz_aisbii(pzapf):
    return pzapf[0] != "fpmsni" and pzapf[-1] == "ieem"
def is_qrrz_irhh(pzapf):
    return not (is_qrrz_ehmlbs(pzapf) or is_qrrz_aisbii(pzapf))
qrrz= Factor("qrrz", [DerivedLevel("ehmlbs", Transition(is_qrrz_ehmlbs, [pzapf])), DerivedLevel("aisbii", Transition(is_qrrz_aisbii, [pzapf])), DerivedLevel("irhh", Transition(is_qrrz_irhh, [pzapf]))])

design=[pzapf,qrrz]
crossing=[qrrz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END