from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xcgfv = Factor("xcgfv", ["tffb","vjlc","qayz","gsq","suinjh","pbu","zxeg"])
def akb(xcgfv):
     return xcgfv[-3] == "vjlc" and not xcgfv[0] == "vjlc"
def hyta(xcgfv):
     return xcgfv[-3] != "vjlc" and  "qayz" == xcgfv[0]
def anlv(xcgfv):
     return (not akb(xcgfv)) and (not xcgfv[0] == "qayz")
fbpa = DerivedLevel("lbxs", Window(akb, [xcgfv],4,1))
zow = DerivedLevel("wacr", Window(hyta, [xcgfv],4,1))
vukla = DerivedLevel("gvvjvb", Window(anlv, [xcgfv],4,1))
mzsjo = Factor("fek", [fbpa, zow, vukla])

### EXPERIMENT
design=[xcgfv,mzsjo]
crossing=[mzsjo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END