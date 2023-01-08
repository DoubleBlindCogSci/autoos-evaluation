from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cxqwa= Factor("cxqwa", ["bsg","zzno","rvjwfw","jdwzg","oaqgpa","xeeur","vep"])
ndwb= Factor("ndwb", ["ccig","dltlx","mhbvc","wpiuz","frtr","oexnrm","sndfb"])
def is_zdv_pjecu(cxqwa, ndwb):
    return cxqwa[0] == "oaqgpa" and ndwb[-1] != "oexnrm"
def is_zdv_fjli(cxqwa, ndwb):
    return not is_zdv_pjecu(cxqwa, ndwb)
zdv= Factor("zdv", [DerivedLevel("pjecu", Transition(is_zdv_pjecu, [cxqwa, ndwb])), DerivedLevel("fjli", Transition(is_zdv_fjli, [cxqwa, ndwb]))])

design=[cxqwa,ndwb,zdv]
crossing=[zdv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END
