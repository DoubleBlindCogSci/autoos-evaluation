from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
spa= Factor("spa", ["nouxqd","rvf","iuy","cnbp","arllcs","gioiz"])
def is_fnugna_uudtil(spa):
    return spa[-1] == "iuy" and spa[0] != "gioiz"
def is_fnugna_pvec(spa):
    return spa[-1] != "iuy" and spa[0] == "gioiz"
def is_fnugna_aeshf(spa):
    return not (is_fnugna_uudtil(spa) or is_fnugna_pvec(spa))
fnugna= Factor("fnugna", [DerivedLevel("uudtil", Transition(is_fnugna_uudtil, [spa])), DerivedLevel("pvec", Transition(is_fnugna_pvec, [spa])), DerivedLevel("aeshf", Transition(is_fnugna_aeshf, [spa]))])

design=[spa,fnugna]
crossing=[fnugna]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
