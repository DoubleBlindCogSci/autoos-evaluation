from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ninu = Factor("ninu", ["bkkl","nxmjre","kbmc","ujbh","fge","smiik"])
def lyed(ninu):
     return ninu[0] == "nxmjre" and not ninu[-1] == "ujbh"
def jnx(ninu):
     return (not "nxmjre" != ninu[0]) and  "ujbh" == ninu[-1]
def wnt(ninu):
     return (ninu[0] != "nxmjre") and (ninu[-1] != "ujbh")
vmrl = DerivedLevel("omq", Transition(lyed, [ninu]))
jpb = DerivedLevel("fgtggu", Transition(jnx, [ninu]))
xxe = DerivedLevel("lkwyt", Transition(wnt, [ninu]))
wwzqr = Factor("jjo", [vmrl, jpb, xxe])

### EXPERIMENT
design=[ninu,wwzqr]
crossing=[wwzqr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_3"))
### END