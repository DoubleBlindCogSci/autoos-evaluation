from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tvzg = Factor("tvzg", ["frf","qjrlhh","hpu","xdpkxt","outoi","yhsj"])
def dgblmw(tvzg):
    return tvzg == "hpu" and tvzg == "outoi"
def dau(tvzg):
    return not (tvzg == "hpu") or not (tvzg == "outoi")
djoum = Factor("igpbb", [DerivedLevel("aijl", WithinTrial(dgblmw, [tvzg])), DerivedLevel("ccs", WithinTrial(dau, [tvzg]))])
### EXPERIMENT
design=[tvzg,djoum]
crossing=[djoum]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END