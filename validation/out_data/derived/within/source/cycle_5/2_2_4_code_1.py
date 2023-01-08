from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
jev = Factor("jev", ["gghyz","zluu","rbqqxc","ryhkz","xeq","fhy","fyjc"])
blwgn = Factor("blwgn", ["myq","ogy","pznd","gvzit","aag"])
def ccpyat(jev, blwgn):
    return jev == "xeq" or blwgn == "myq"
def szzzgw(jev,blwgn):
    return not ccpyat(jev, blwgn)
plgh = Factor("uhghv", [DerivedLevel("flbae", WithinTrial(ccpyat, [jev, blwgn])), DerivedLevel("uopsq", WithinTrial(szzzgw, [jev, blwgn]))])
### EXPERIMENT
design=[jev,blwgn,plgh]
crossing=[plgh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END