from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tnrF='s^ryhRRE@v'
wsJ44aXInZ_=Factor('klWxvR',['isc2IlmXIX',"JLcUIfY","cDlenobc",Level(';Az',9),tnrF,'B~L@$',"f^Ty",Level("JcbwJCsZt",1),'@bMmDp!x',"SScdTo5n#Edad"])

### EXPERIMENT
design=[wsJ44aXInZ_]
crossing=[wsJ44aXInZ_]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/9_1_0"))
### END