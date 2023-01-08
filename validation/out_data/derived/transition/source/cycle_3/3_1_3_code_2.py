from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ninu = Factor("ninu", ["bkkl","nxmjre","kbmc","ujbh","fge","smiik"])
def is_jjo_omq(ninu):
    return ninu[-1] == "nxmjre" and ninu[0] != "ujbh"
def is_jjo_fgtggu(ninu):
    return ninu[-1] != "nxmjre" and ninu[0] == "ujbh"
def is_jjo_lkwyt(ninu):
    return not (is_jjo_omq(ninu) or is_jjo_fgtggu(ninu))
jjo= Factor("jjo", [DerivedLevel("omq", Transition(is_jjo_omq, [ninu])), DerivedLevel("fgtggu", Transition(is_jjo_fgtggu, [ninu])), DerivedLevel("lkwyt", Transition(is_jjo_lkwyt, [ninu]))])

design=[ninu,jjo]
crossing=[jjo]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_3"))

### END
