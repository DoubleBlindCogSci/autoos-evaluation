from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
owzrxv = Factor("owzrxv", ["grm","mpo","zvtm","fen","uazuyb"])
def zlco(owzrxv):
    return owzrxv == "mpo"
def umufa(owzrxv):
    return owzrxv != "mpo"
auu = DerivedLevel("ywhum", WithinTrial(zlco, [owzrxv]))
yuiiy = DerivedLevel("lfq", WithinTrial(umufa, [owzrxv]))
ocg = Factor("xqet", [auu, yuiiy])

### EXPERIMENT
design=[owzrxv,ocg]
crossing=[ocg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END