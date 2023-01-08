from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zywlx = Factor("zywlx", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
vtdezu = Factor("vtdezu", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
ardkv = Factor("ardkv", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
def hzoc(zywlx, ardkv, vtdezu):
    return zywlx[0] == ardkv[-2]
def slwu(zywlx, ardkv, vtdezu):
    return not hzoc(zywlx, ardkv, vtdezu)
xwiea = Factor("sztux", [DerivedLevel("rjsv", Window(hzoc, [zywlx, vtdezu, ardkv],3,1)), DerivedLevel("kem", Window(slwu, [zywlx, vtdezu, ardkv],3,1))])
### EXPERIMENT
design=[zywlx,vtdezu,ardkv,xwiea]
crossing=[xwiea]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END