from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
axm = Factor("axm", ["zyzi","oblzx","partw","ztbn","yfpy","qoh","qgwsjr"])
def ljn(axm):
    return axm[-2] != "oblzx" and axm[-1] == "qgwsjr"
def eviihp(axm):
    return not ljn(axm)
lnpeu = Factor("xex", [DerivedLevel("vdxf", Window(ljn, [axm],3,1)), DerivedLevel("dixnld", Window(eviihp, [axm],3,1))])
### EXPERIMENT
design=[axm,lnpeu]
crossing=[lnpeu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END