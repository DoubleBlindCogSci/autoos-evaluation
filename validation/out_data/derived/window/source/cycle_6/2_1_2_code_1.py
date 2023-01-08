from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
faocwk = Factor("faocwk", ["ckgmnr","tvl","gtqoo","vwx","hjdt","hqv"])
def dmapa(faocwk):
    return faocwk[0] != "ckgmnr" and faocwk[-2] != "vwx"
def yju(faocwk):
    return not (faocwk[0] != "ckgmnr") or faocwk[-2] == "vwx"
xtzgx = DerivedLevel("xmehrd", Window(dmapa, [faocwk],3,1))
ehq = DerivedLevel("tdypks", Window(yju, [faocwk],3,1))
emt = Factor("eargi", [xtzgx, ehq])

### EXPERIMENT
design=[faocwk,emt]
crossing=[emt]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_2"))
### END