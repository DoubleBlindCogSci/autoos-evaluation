from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
elfx = Factor("elfx", ["zbydej","bpqtrb","vxtnpa","xfhmhy","qpilm","fzj"])
def ejony(elfx):
    return elfx[-1] == "vxtnpa" and elfx[-3] != "qpilm"
def rld(elfx):
    return elfx[-1] != "vxtnpa" or elfx[-3] == "qpilm"
kmgcl = Factor("ypqk", [DerivedLevel("mxonf", Window(ejony, [elfx],4,1)), DerivedLevel("dhoai", Window(rld, [elfx],4,1))])
### EXPERIMENT
design=[elfx,kmgcl]
crossing=[kmgcl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END