from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
djaod = Factor("djaod", ["mheqs","aewzew","pokcw","jlr","xvdbtl","qednx","job"])
moccj = Factor("moccj", ["awupod","zuyzk","butf","ybg","aywgfe"])
def is_rcxfsi_ocebmw(djaod, moccj):
    return djaod[-1] != "xvdbtl" and moccj[0] == "aywgfe"
def is_rcxfsi_ysotd(djaod, moccj):
    return not is_rcxfsi_ocebmw(djaod, moccj)
rcxfsi = Factor("rcxfsi", [DerivedLevel("ocebmw", Window(is_rcxfsi_ocebmw, [djaod, moccj], 2, 1)), DerivedLevel("ysotd", Window(is_rcxfsi_ysotd, [djaod, moccj], 2, 1))])

design=[djaod,moccj,rcxfsi]
crossing=[rcxfsi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END