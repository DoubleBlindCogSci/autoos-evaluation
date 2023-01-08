from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
varpxe = Factor("varpxe", ["slql","kkzoxv","hdloe","wffdn","eudjn","vdw"])
def oay(varpxe):
     return "eudjn" == varpxe
def anhcav(varpxe):
     return "vdw" == varpxe
def seh(varpxe):
     return (not varpxe == "eudjn") and (not anhcav(varpxe))
xahcg = Factor("ntabf", [DerivedLevel("kon", WithinTrial(oay, [varpxe])), DerivedLevel("kzist", WithinTrial(anhcav, [varpxe])),DerivedLevel("qab", WithinTrial(seh, [varpxe]))])
### EXPERIMENT
design=[varpxe,xahcg]
crossing=[xahcg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_1"))
### END