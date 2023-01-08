from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ngavjj = Factor("ngavjj", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
umnwpc = Factor("umnwpc", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
kibvon = Factor("kibvon", ["ips","ych","kwmfoj","fedhn","oflobf","nym","owwhzk","mscp"])
def piwi(ngavjj, kibvon, umnwpc):
     return kibvon == ngavjj
def tbrv(ngavjj, kibvon, umnwpc):
     return kibvon != ngavjj and ngavjj == umnwpc
def bhoiqy(ngavjj, kibvon, umnwpc):
     return (not piwi(ngavjj, kibvon, umnwpc)) and (not tbrv(ngavjj, kibvon, umnwpc))
zfb = DerivedLevel("hysx", WithinTrial(piwi, [ngavjj, umnwpc, kibvon]))
axej = DerivedLevel("gmaul", WithinTrial(tbrv, [ngavjj, umnwpc, kibvon]))
fvpdcn = DerivedLevel("vipame", WithinTrial(bhoiqy, [ngavjj, umnwpc, kibvon]))
mnx = Factor("egudg", [zfb, axej, fvpdcn])

### EXPERIMENT
design=[ngavjj,umnwpc,kibvon,mnx]
crossing=[mnx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END