from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ejs = Factor("ejs", ["zrpmdz","pjkm","gzdyua","jmxf","aqb"])
def knzdv(ejs):
    return ejs != "jmxf" and ejs == "gzdyua"
def era(ejs):
    return not knzdv(ejs)
sal = Factor("cxtdwa", [DerivedLevel("jayarf", WithinTrial(knzdv, [ejs])), DerivedLevel("vxv", WithinTrial(era, [ejs]))])
### EXPERIMENT
design=[ejs,sal]
crossing=[sal]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END