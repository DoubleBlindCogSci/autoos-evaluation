from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
yvt = Factor("yvt", ["aspg", "mypy"])
nwy = Factor("nwy", ["ludty", "sniosf"])
shy = Factor("shy", ["aspg", "mypy"])
yvnfyr = Factor("yvnfyr", ["ludty", "sniosf"])
eqhnnb = Factor("eqhnnb", ["xjf", "oxjjzy"])
def is_cdf_rprpk(eqhnnb, yvt):
    return eqhnnb == yvt
def is_cdf_zydsnt(eqhnnb, yvt):
    return not is_cdf_rprpk(eqhnnb, yvt)
cdf = Factor("cdf", [DerivedLevel("rprpk", WithinTrial(is_cdf_rprpk, [eqhnnb, yvt])), DerivedLevel("zydsnt", WithinTrial(is_cdf_zydsnt, [eqhnnb, yvt]))])
constraints = [AtMostKInARow(4, yvt), MinimumTrials(32)]
crossing = [yvt, yvnfyr]

design=[yvt,nwy,shy,yvnfyr,eqhnnb,cdf]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_2"))
