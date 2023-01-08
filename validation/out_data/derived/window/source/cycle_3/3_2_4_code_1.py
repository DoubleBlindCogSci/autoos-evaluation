from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
sfjmyp = Factor("sfjmyp", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
upld = Factor("upld", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
wroo = Factor("wroo", ["byohcl","gvcnj","zxdl","yeu","xptcy","bok"])
def hlhwk(sfjmyp, wroo, upld):
     return sfjmyp[0] == wroo[-2] and sfjmyp[-2] != upld[0]
def ayxh(sfjmyp, wroo, upld):
     return wroo[-2] != sfjmyp[0] and sfjmyp[-2] == upld[0]
def dvnaw(sfjmyp, wroo, upld):
     return (not sfjmyp[0] == wroo[-2]) and (not sfjmyp[-2] == upld[0])
mnz = Factor("qykga", [DerivedLevel("kkgk", Window(hlhwk, [sfjmyp, upld, wroo],3,1)), DerivedLevel("jpv", Window(ayxh, [sfjmyp, upld, wroo],3,1)),DerivedLevel("wzrc", Window(dvnaw, [sfjmyp, upld, wroo],3,1))])
### EXPERIMENT
design=[sfjmyp,upld,wroo,mnz]
crossing=[mnz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_4"))
### END