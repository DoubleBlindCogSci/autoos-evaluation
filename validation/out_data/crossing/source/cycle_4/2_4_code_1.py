from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vxm = Factor("vxm", ["kadgb", "ikjefh"])
lnn = Factor("lnn", ["zzci", "xxgym"])
ligxx = Factor("ligxx", ["zeyh", "pnwt"])
zfvaeo = Factor("zfvaeo", ["usnsnu", "zclxb"])

### EXPERIMENT
design=[vxm,lnn,ligxx,zfvaeo]
crossing=[[vxm,lnn,ligxx],[zfvaeo],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_4"))
### END