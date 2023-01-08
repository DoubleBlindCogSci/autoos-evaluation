from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sxud = Factor("sxud", ["jnd", "ifwp"])
mew = Factor("mew", ["esidn", "lrz"])
zamss = Factor("zamss", ["uskak", "avemq"])
badrp = Factor("badrp", ["ulhdwc", "bieqn"])
bnuavc = Factor("bnuavc", ["wcw", "xocwd"])

### EXPERIMENT
design=[sxud,mew,zamss,badrp,bnuavc]
crossing=[[sxud,mew],[zamss,badrp,bnuavc],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1"))
### END