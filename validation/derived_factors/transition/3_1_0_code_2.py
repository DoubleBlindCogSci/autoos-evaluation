from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ahpu = Factor("ahpu", ["uha","kfgvi","vfifq","vwqq","yza","kbq"])
def is_xzsh_dhvhl(ahpu):
    return ahpu[0] == "kbq" and ahpu[-1] != "vwqq"
def is_xzsh_ysbhd(ahpu):
    return ahpu[0] != "kbq" and ahpu[-1] == "vwqq"
def is_xzsh_ryb(ahpu):
    return not (is_xzsh_dhvhl(ahpu) or is_xzsh_ysbhd(ahpu))
xzsh = Factor("xzsh", [DerivedLevel("dhvhl", Transition(is_xzsh_dhvhl, [ahpu])), DerivedLevel("ysbhd", Transition(is_xzsh_ysbhd, [ahpu])), DerivedLevel("ryb", Transition(is_xzsh_ryb, [ahpu]))])

design=[ahpu,xzsh]
crossing=[xzsh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END