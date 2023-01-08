from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jev = Factor("jev", ["gghyz","zluu","rbqqxc","ryhkz","xeq","fhy","fyjc"])
blwgn = Factor("blwgn", ["myq","ogy","pznd","gvzit","aag"])
def is_uhghv_flbae(jev, blwgn):
    return jev == "xeq" or blwgn == "myq"
def is_uhghv_uopsq(jev, blwgn):
    return not is_uhghv_flbae(jev, blwgn)
uhghv = Factor("uhghv", [DerivedLevel("flbae", WithinTrial(is_uhghv_flbae, [jev, blwgn])), DerivedLevel("uopsq", WithinTrial(is_uhghv_uopsq, [jev, blwgn]))])

design=[jev,blwgn,uhghv]
crossing=[uhghv]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_4"))

### END