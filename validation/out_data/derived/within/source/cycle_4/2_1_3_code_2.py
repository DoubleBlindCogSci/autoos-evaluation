from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
owzrxv = Factor("owzrxv", ["grm","mpo","zvtm","fen","uazuyb"])
def is_xqet_ywhum(owzrxv):
    return owzrxv == "mpo"
def is_xqet_lfq(owzrxv):
    return not is_xqet_ywhum(owzrxv)
xqet = Factor("xqet", [DerivedLevel("ywhum", WithinTrial(is_xqet_ywhum, [owzrxv])), DerivedLevel("lfq", WithinTrial(is_xqet_lfq, [owzrxv]))])

design=[owzrxv,xqet]
crossing=[xqet]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END