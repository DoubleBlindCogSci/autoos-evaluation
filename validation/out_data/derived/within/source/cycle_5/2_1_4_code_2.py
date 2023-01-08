from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xczrq = Factor("xczrq", ["doby","xtplr","zfv","echghq","esnx","xhfanc","hune"])
def is_rmg_njy(xczrq):
    return xczrq != "zfv"
def is_rmg_bqgh(xczrq):
    return not is_rmg_njy(xczrq)
rmg = Factor("rmg", [DerivedLevel("njy", WithinTrial(is_rmg_njy, [xczrq])), DerivedLevel("bqgh", WithinTrial(is_rmg_bqgh, [xczrq]))])

design=[xczrq,rmg]
crossing=[rmg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END