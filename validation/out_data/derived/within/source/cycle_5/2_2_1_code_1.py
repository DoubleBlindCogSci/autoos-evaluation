from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rrrwbm = Factor("rrrwbm", ["fwn","vxk","tvzqzp","ekjdo","ntfbnx","boa"])
otwro = Factor("otwro", ["qeyapa","wbjzs","jvp","eoqmdg","iututk"])
def bfstcr(rrrwbm, otwro):
    return rrrwbm == "tvzqzp" or otwro != "jvp"
def tcrbpf(rrrwbm,otwro):
    return rrrwbm != "tvzqzp" and not (otwro != "jvp")
qhzbm = Factor("fzsz", [DerivedLevel("mlupf", WithinTrial(bfstcr, [rrrwbm, otwro])), DerivedLevel("bhy", WithinTrial(tcrbpf, [rrrwbm, otwro]))])
### EXPERIMENT
design=[rrrwbm,otwro,qhzbm]
crossing=[qhzbm]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END