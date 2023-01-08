from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
bsszxa = Factor("bsszxa", ["qbylzt","qwco","mzknpx","vcov","qmkypw","mzhdya","ijd"])
def kpyp(bsszxa):
     return bsszxa[0] == "qwco" and bsszxa[-1] != "qbylzt"
def phz(bsszxa):
     return (bsszxa[0] != "qwco") and  bsszxa[-1] == "qbylzt"
def ssciw(bsszxa):
     return (bsszxa[0] != "qwco") and (not bsszxa[-1] == "qbylzt")
duxz = Factor("vacdzn", [DerivedLevel("aaiu", Transition(kpyp, [bsszxa])), DerivedLevel("plu", Transition(phz, [bsszxa])),DerivedLevel("gusq", Transition(ssciw, [bsszxa]))])
### EXPERIMENT
design=[bsszxa,duxz]
crossing=[duxz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END