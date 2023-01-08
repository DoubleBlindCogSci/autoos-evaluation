from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lrlvkb = Factor("lrlvkb", ["xdm", "omt"])
bcuuqr = Factor("bcuuqr", ["ghui", "daqwq"])
etqenb = Factor("etqenb", ["fcajbk", "prbzrx"])
oyir = Factor("oyir", ["hkj", "zulbj"])

### EXPERIMENT
design=[lrlvkb,bcuuqr,etqenb,oyir]
crossing=[[lrlvkb],[bcuuqr,etqenb],[oyir],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END