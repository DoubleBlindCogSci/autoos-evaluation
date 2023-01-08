from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xcgfv = Factor("xcgfv", ["tffb","vjlc","qayz","gsq","suinjh","pbu","zxeg"])
def is_fek_lbxs(xcgfv):
    return xcgfv[-3] == "vjlc" and xcgfv[0] != "vjlc"
def is_fek_wacr(xcgfv):
    return xcgfv[-3] != "vjlc" and xcgfv[0] == "qayz"
def is_fek_gvvjvb(xcgfv):
    return not (is_fek_lbxs(xcgfv) or is_fek_wacr(xcgfv))
fek= Factor("fek", [DerivedLevel("lbxs", Window(is_fek_lbxs, [xcgfv], 4, 1)), DerivedLevel("wacr", Window(is_fek_wacr, [xcgfv], 4, 1)), DerivedLevel("gvvjvb", Window(is_fek_gvvjvb, [xcgfv], 4, 1))])

design=[xcgfv,fek]
crossing=[fek]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END
