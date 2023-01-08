from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rrrwbm = Factor("rrrwbm", ["fwn","vxk","tvzqzp","ekjdo","ntfbnx","boa"])
otwro = Factor("otwro", ["qeyapa","wbjzs","jvp","eoqmdg","iututk"])
def is_fzsz_mlupf(rrrwbm, otwro):
    return rrrwbm == "tvzqzp" or otwro != "jvp"
def is_fzsz_bhy(rrrwbm, otwro):
    return not is_fzsz_mlupf(rrrwbm, otwro)
fzsz = Factor("fzsz", [DerivedLevel("mlupf", WithinTrial(is_fzsz_mlupf, [rrrwbm, otwro])), DerivedLevel("bhy", WithinTrial(is_fzsz_bhy, [rrrwbm, otwro]))])

design=[rrrwbm,otwro,fzsz]
crossing=[fzsz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END