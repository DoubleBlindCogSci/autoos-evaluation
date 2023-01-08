from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
swz= Factor("swz", ["ucnqkl","gxliu","wsxdz","gtlksr","bii","xdtrys"])

def is_sxq_zlxf(swz):
    return swz == "gxliu"
def is_sxq_bjfgc(swz):
    return swz == "bii"
def is_sxq_cuouqr(swz):
    return not (is_sxq_zlxf(swz) or is_sxq_bjfgc(swz))
sxq= Factor("sxq", [DerivedLevel("zlxf", WithinTrial(is_sxq_zlxf, [swz])), DerivedLevel("bjfgc", WithinTrial(is_sxq_bjfgc, [swz])), DerivedLevel("cuouqr", WithinTrial(is_sxq_cuouqr, [swz]))])


design=[swz,sxq]
crossing=[sxq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
