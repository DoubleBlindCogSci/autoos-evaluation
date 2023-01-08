from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qdjc = Factor("qdjc", ["itphwq","qrozor","yljayi","aclc","oflg","qdvrnh"])
def is_erywow_ievvxv(qdjc):
    return qdjc == "qrozor" or qdjc == "oflg"
def is_erywow_tai(qdjc):
    return not is_erywow_ievvxv(qdjc)
erywow = Factor("erywow", [DerivedLevel("ievvxv", WithinTrial(is_erywow_ievvxv, [qdjc])), DerivedLevel("tai", WithinTrial(is_erywow_tai, [qdjc]))])

design=[qdjc,erywow]
crossing=[erywow]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END