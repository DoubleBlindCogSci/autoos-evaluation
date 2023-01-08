from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ejs = Factor("ejs", ["zrpmdz","pjkm","gzdyua","jmxf","aqb"])
def is_cxtdwa_jayarf(ejs):
    return ejs != "jmxf" and ejs == "gzdyua"
def is_cxtdwa_vxv(ejs):
    return not is_cxtdwa_jayarf(ejs)
cxtdwa = Factor("cxtdwa", [DerivedLevel("jayarf", WithinTrial(is_cxtdwa_jayarf, [ejs])), DerivedLevel("vxv", WithinTrial(is_cxtdwa_vxv, [ejs]))])

design=[ejs,cxtdwa]
crossing=[cxtdwa]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END