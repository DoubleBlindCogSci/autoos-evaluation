from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dmjbcm = Factor("dmjbcm", ["trcg","optgu","aahlc","udmppq","kiywln","hza"])
def ixlvj(dmjbcm):
     return "kiywln" == dmjbcm[-2] and not dmjbcm[-1] == "kiywln"
def joisbh(dmjbcm):
     return dmjbcm[-2] != "kiywln" and  dmjbcm[-1] == "aahlc"
def khhps(dmjbcm):
     return (not dmjbcm[-2] == "kiywln") and (dmjbcm[-1] != "aahlc")
vzgrb = Factor("hhvfof", [DerivedLevel("aljh", Window(ixlvj, [dmjbcm],3,1)), DerivedLevel("mdvn", Window(joisbh, [dmjbcm],3,1)),DerivedLevel("qie", Window(khhps, [dmjbcm],3,1))])
### EXPERIMENT
design=[dmjbcm,vzgrb]
crossing=[vzgrb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_4"))
### END