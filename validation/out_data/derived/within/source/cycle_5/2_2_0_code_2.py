from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dfsft = Factor("dfsft", ["zbvh","vwozf","iqyms","igkz","gsigmk","fnasp"])
ork = Factor("ork", ["wjkt","eer","tmsql","pbjt","hljjf","knenyj"])
def is_ltll_ryr(dfsft, ork):
    return dfsft == "iqyms" or ork != "eer"
def is_ltll_waeeu(dfsft, ork):
    return not is_ltll_ryr(dfsft, ork)
ltll = Factor("ltll", [DerivedLevel("ryr", WithinTrial(is_ltll_ryr, [dfsft, ork])), DerivedLevel("waeeu", WithinTrial(is_ltll_waeeu, [dfsft, ork]))])

design=[dfsft,ork,ltll]
crossing=[ltll]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END