from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qdjc = Factor("qdjc", ["itphwq","qrozor","yljayi","aclc","oflg","qdvrnh"])
def eswu(qdjc):
    return qdjc == "qrozor" or qdjc == "oflg"
def axw(qdjc):
    return not (qdjc == "qrozor") and not (qdjc == "oflg")
rlxzlr = Factor("erywow", [DerivedLevel("ievvxv", WithinTrial(eswu, [qdjc])), DerivedLevel("tai", WithinTrial(axw, [qdjc]))])
### EXPERIMENT
design=[qdjc,rlxzlr]
crossing=[rlxzlr]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END