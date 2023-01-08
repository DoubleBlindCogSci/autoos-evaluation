from sweetpea import *
import os
_dir=os.path.dirname(__file__)
kibg = Factor("kibg", ["ohmm", "jatpa"])
jdkczs = Factor("jdkczs", ["hrtz", "yefe"])
vzy = Factor("vzy", ["chy", "rhvm"])
constraints = []
crossing = [kibg, jdkczs, vzy]


design=[kibg,jdkczs,vzy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END