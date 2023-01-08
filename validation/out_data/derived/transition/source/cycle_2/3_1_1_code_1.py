from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
spa = Factor("spa", ["nouxqd","rvf","iuy","cnbp","arllcs","gioiz"])
def zejlc(spa):
     return "iuy" == spa[0] and spa[-1] != "gioiz"
def adiz(spa):
     return (not "iuy" != spa[0]) and  spa[-1] == "gioiz"
def ygmul(spa):
     return (not spa[0] == "iuy") and (spa[-1] != "gioiz")
dua = DerivedLevel("uudtil", Transition(zejlc, [spa]))
bgq = DerivedLevel("pvec", Transition(adiz, [spa]))
wufdvg = DerivedLevel("aeshf", Transition(ygmul, [spa]))
ozig = Factor("fnugna", [dua, bgq, wufdvg])

### EXPERIMENT
design=[spa,ozig]
crossing=[ozig]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END