from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ujghq = Factor("ujghq", ["ptz", "dxkffl"])
pmxb = Factor("pmxb", ["pvyjyc", "zumlf"])
bxst = Factor("bxst", ["tayjxe", "hhxpo"])
tmk = Factor("tmk", ["nus", "czsoi"])

### EXPERIMENT
design=[ujghq,pmxb,bxst,tmk]
crossing=[[ujghq,pmxb,bxst,tmk]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2"))
### END