from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uvga = Factor("uvga", ["sus","wveejv","dspvo","wqq","pwne","gnh"])
vinzl = Factor("vinzl", ["ida","hcf","wfw","szed","uhvpm","pwfe"])
def ovb(uvga, vinzl):
     return uvga == "wqq"
def wkg(uvga, vinzl):
     return uvga != "wqq" and  vinzl == "uhvpm"
def uon(uvga, vinzl):
     return (not uvga == "wqq") and (not vinzl == "uhvpm")
ajbcj = Factor("xtl", [DerivedLevel("sudue", WithinTrial(ovb, [uvga, vinzl])), DerivedLevel("xmjku", WithinTrial(wkg, [uvga, vinzl])),DerivedLevel("cxlk", WithinTrial(uon, [uvga, vinzl]))])
### EXPERIMENT
design=[uvga,vinzl,ajbcj]
crossing=[ajbcj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_3"))
### END