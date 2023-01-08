from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zywlx = Factor("zywlx", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
vtdezu = Factor("vtdezu", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
ardkv = Factor("ardkv", ["euvw","nfnp","gkwnzh","rhhg","srqgm","vxn","ayq"])
def is_sztux_rjsv(zywlx, ardkv, vtdezu):
    return zywlx[0] == ardkv[-2]
def is_sztux_kem(zywlx, ardkv, vtdezu):
    return not is_sztux_rjsv(zywlx, ardkv, vtdezu)
sztux = Factor("sztux", [DerivedLevel("rjsv", Window(is_sztux_rjsv, [zywlx, ardkv, vtdezu], 3, 1)), DerivedLevel("kem", Window(is_sztux_kem, [zywlx, ardkv, vtdezu], 3, 1))])

design=[zywlx,vtdezu,ardkv,sztux]
crossing=[sztux]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END