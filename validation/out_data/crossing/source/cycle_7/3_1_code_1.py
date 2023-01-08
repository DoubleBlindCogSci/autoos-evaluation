from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
kibg = Factor("kibg", ["ohmm", "jatpa"])
jdkczs = Factor("jdkczs", ["hrtz", "yefe"])
vzy = Factor("vzy", ["chy", "rhvm"])

### EXPERIMENT
design=[kibg,jdkczs,vzy]
crossing=[[kibg,jdkczs,vzy]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1"))
### END