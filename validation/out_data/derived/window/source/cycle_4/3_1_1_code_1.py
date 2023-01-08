from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pqdejc = Factor("pqdejc", ["yhvz","vumfbe","tavubn","okanp","hoaem","edsktp"])
def rlaxgv(pqdejc):
     return "okanp" == pqdejc[0] and not pqdejc[-2] == "okanp"
def bejfjg(pqdejc):
     return not "okanp" == pqdejc[0] and  "edsktp" == pqdejc[-2]
def lrqw(pqdejc):
     return (not pqdejc[0] == "okanp") and (not bejfjg(pqdejc))
qaift = DerivedLevel("ksm", Window(rlaxgv, [pqdejc],3,1))
sywlo = DerivedLevel("njg", Window(bejfjg, [pqdejc],3,1))
uxgs = DerivedLevel("dbkie", Window(lrqw, [pqdejc],3,1))
davyh = Factor("piqz", [qaift, sywlo, uxgs])

### EXPERIMENT
design=[pqdejc,davyh]
crossing=[davyh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END