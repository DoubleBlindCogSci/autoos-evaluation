from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
axm = Factor("axm", ["zyzi","oblzx","partw","ztbn","yfpy","qoh","qgwsjr"])
def is_xex_vdxf(axm):
    return axm[-2] != "oblzx" and axm[-1] == "qgwsjr"
def is_xex_dixnld(axm):
    return not is_xex_vdxf(axm)
xex = Factor("xex", [DerivedLevel("vdxf", Window(is_xex_vdxf, [axm], 3, 1)), DerivedLevel("dixnld", Window(is_xex_dixnld, [axm], 3, 1))])

design=[axm,xex]
crossing=[xex]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END