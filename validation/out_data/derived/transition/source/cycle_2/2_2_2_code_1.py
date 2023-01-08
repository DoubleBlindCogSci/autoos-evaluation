from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cxqwa = Factor("cxqwa", ["bsg","zzno","rvjwfw","jdwzg","oaqgpa","xeeur","vep"])
ndwb = Factor("ndwb", ["ccig","dltlx","mhbvc","wpiuz","frtr","oexnrm","sndfb"])
def bpcper(cxqwa, ndwb):
    return cxqwa[0] == "oaqgpa" and ndwb[-1] != "oexnrm"
def mgzbba(cxqwa,ndwb):
    return not bpcper(cxqwa, ndwb)
wppdl = Factor("zdv", [DerivedLevel("pjecu", Transition(bpcper, [cxqwa, ndwb])), DerivedLevel("fjli", Transition(mgzbba, [cxqwa, ndwb]))])
### EXPERIMENT
design=[cxqwa,ndwb,wppdl]
crossing=[wppdl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END