from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
phtdz = Factor("phtdz", ["gll", "ycyfc"])
yhe = Factor("yhe", ["yex", "cmaggf"])
kdvs = Factor("kdvs", ["rkji", "lzxx"])
rkxnnh = Factor("rkxnnh", ["uhv", "ywjj"])
lcvz = Factor("lcvz", ["btiau", "aff"])
sats = Factor("sats", ["hwo", "vvkte"])

### EXPERIMENT
design=[phtdz,yhe,kdvs,rkxnnh,lcvz,sats]
crossing=[[phtdz,yhe,kdvs,rkxnnh,lcvz,sats]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2"))
### END