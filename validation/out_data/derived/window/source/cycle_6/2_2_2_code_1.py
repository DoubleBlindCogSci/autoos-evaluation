from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
djaod = Factor("djaod", ["mheqs","aewzew","pokcw","jlr","xvdbtl","qednx","job"])
moccj = Factor("moccj", ["awupod","zuyzk","butf","ybg","aywgfe"])
def akrw(djaod, moccj):
    return djaod[-1] != "xvdbtl" and moccj[0] == "aywgfe"
def mjoo(djaod,moccj):
    return not (djaod[-1] != "xvdbtl") or moccj[0] != "aywgfe"
kewu = DerivedLevel("ocebmw", Window(akrw, [djaod, moccj],2,1))
dgp = DerivedLevel("ysotd", Window(mjoo, [djaod, moccj],2,1))
wsah = Factor("rcxfsi", [kewu, dgp])

### EXPERIMENT
design=[djaod,moccj,wsah]
crossing=[wsah]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END