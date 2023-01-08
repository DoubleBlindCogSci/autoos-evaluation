from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zksmic = Factor("zksmic", ["jcy","plf","ugmriq","xezfoh","erjf","figvtg","ztgmq"])
def hee(zksmic):
    return zksmic[-3] != "erjf" and zksmic[-1] == "plf"
def nvvfq(zksmic):
    return not (zksmic[-3] != "erjf") or not (zksmic[-3] == "plf")
jcs = Factor("dhxvi", [DerivedLevel("idwpav", Window(hee, [zksmic],4,1)), DerivedLevel("ihula", Window(nvvfq, [zksmic],4,1))])
### EXPERIMENT
design=[zksmic,jcs]
crossing=[jcs]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_4"))
### END