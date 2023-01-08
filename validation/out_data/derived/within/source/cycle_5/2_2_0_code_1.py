from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dfsft = Factor("dfsft", ["zbvh","vwozf","iqyms","igkz","gsigmk","fnasp"])
ork = Factor("ork", ["wjkt","eer","tmsql","pbjt","hljjf","knenyj"])
def hcsxy(dfsft, ork):
    return dfsft == "iqyms" or ork != "eer"
def vbc(dfsft,ork):
    return not (dfsft == "iqyms") and ork == "eer"
mljgg = Factor("ltll", [DerivedLevel("ryr", WithinTrial(hcsxy, [dfsft, ork])), DerivedLevel("waeeu", WithinTrial(vbc, [dfsft, ork]))])
### EXPERIMENT
design=[dfsft,ork,mljgg]
crossing=[mljgg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END