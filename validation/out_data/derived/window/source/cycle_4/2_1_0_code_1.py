from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
hxtcdr = Factor("hxtcdr", ["qvoo","bmx","tjlgc","ozz","wdedml","bwrbl"])
def mdxwj(hxtcdr):
    return hxtcdr[-3] != "tjlgc" or hxtcdr[0] == "bwrbl"
def hdqpnk(hxtcdr):
    return not (hxtcdr[-3] != "tjlgc") and not (hxtcdr[-3] == "bwrbl")
wtar = DerivedLevel("vtwb", Window(mdxwj, [hxtcdr],4,1))
zurw = DerivedLevel("tzocpv", Window(hdqpnk, [hxtcdr],4,1))
iddzf = Factor("yaeoo", [wtar, zurw])

### EXPERIMENT
design=[hxtcdr,iddzf]
crossing=[iddzf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END