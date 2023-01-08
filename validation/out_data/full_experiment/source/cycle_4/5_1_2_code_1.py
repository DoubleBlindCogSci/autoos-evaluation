from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
yvt = Factor("yvt", ["aspg", "mypy"])
nwy = Factor("nwy", ["ludty", "sniosf"])
shy = Factor("shy", ["aspg", "mypy"])
yvnfyr = Factor("yvnfyr", ["ludty", "sniosf"])
eqhnnb = Factor("eqhnnb", ["xjf", "oxjjzy"])
def jwc (eqhnnb, yvt):
    return eqhnnb == yvt
def msqcoq (eqhnnb, yvt):
    return not jwc(eqhnnb, yvt)
cdf = Factor("cdf", [DerivedLevel("rprpk", WithinTrial(jwc, [eqhnnb, yvt])), DerivedLevel("zydsnt", WithinTrial(msqcoq, [eqhnnb, yvt]))])
design=[cdf,yvt,nwy,shy,yvnfyr,eqhnnb]
constraints=[AtMostKInARow(4, yvt),MinimumTrials(32)]
crossing=[yvt,yvnfyr]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_2"))
