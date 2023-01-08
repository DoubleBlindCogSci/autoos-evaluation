from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
pxep = Factor("pxep", ["nne","wsv","rjpz","dtklx","yiuulv"])
knuuf = Factor("knuuf", ["nne","wsv","rjpz","dtklx","yiuulv"])
yzw = Factor("yzw", ["nne","wsv","rjpz","dtklx","yiuulv"])
def njxbq(pxep, knuuf, yzw):
    return pxep != knuuf or pxep != yzw
def yjyoap(pxep, knuuf, yzw):
    return not (pxep != knuuf) and pxep == yzw
dlxu = DerivedLevel("jlyb", WithinTrial(njxbq, [pxep, knuuf, yzw]))
goq = DerivedLevel("uryvz", WithinTrial(yjyoap, [pxep, knuuf, yzw]))
yyu = Factor("gzrvlk", [dlxu, goq])

### EXPERIMENT
design=[pxep,knuuf,yzw,yyu]
crossing=[yyu]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_3"))
### END