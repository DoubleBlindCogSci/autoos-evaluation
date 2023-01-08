from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qasz= Factor("qasz", ["optefg","usdn","pdehkm","eiyzf","jyxdrm","hoq"])
def is_uix_mzrq(qasz):
    return qasz[0] != "jyxdrm" and qasz[0] != "optefg"
def is_uix_bfurc(qasz):
    return not is_uix_mzrq(qasz)
uix= Factor("uix", [DerivedLevel("mzrq", Window(is_uix_mzrq, [qasz], 4, 1)), DerivedLevel("bfurc", Window(is_uix_bfurc, [qasz], 4, 1))])

design=[qasz,uix]
crossing=[uix]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END
