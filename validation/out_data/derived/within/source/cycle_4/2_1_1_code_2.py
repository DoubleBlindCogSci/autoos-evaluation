from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pva = Factor("pva", ["uzzge","chl","bemjj","tzm","qxlo"])
def is_zolw_lqfnc(pva):
    return pva != "uzzge" and pva != "qxlo"
def is_zolw_elroif(pva):
    return not is_zolw_lqfnc(pva)
zolw= Factor("zolw", [DerivedLevel("lqfnc", WithinTrial(is_zolw_lqfnc, [pva])), DerivedLevel("elroif", WithinTrial(is_zolw_elroif, [pva]))])

design=[pva,zolw]
crossing=[zolw]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END