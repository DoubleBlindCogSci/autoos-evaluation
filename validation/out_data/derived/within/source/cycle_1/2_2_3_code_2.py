from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pxep= Factor("pxep", ["nne","wsv","rjpz","dtklx","yiuulv"])
knuuf= Factor("knuuf", ["nne","wsv","rjpz","dtklx","yiuulv"])
yzw= Factor("yzw", ["nne","wsv","rjpz","dtklx","yiuulv"])

def is_gzrvlk_jlyb(pxep, knuuf, yzw):
    return pxep != knuuf or pxep != yzw
def is_gzrvlk_uryvz(pxep, knuuf, yzw):
    return pxep == knuuf and pxep == yzw
gzrvlk= Factor("gzrvlk", [DerivedLevel("jlyb", WithinTrial(is_gzrvlk_jlyb, [pxep, knuuf, yzw])), DerivedLevel("uryvz", WithinTrial(is_gzrvlk_uryvz, [pxep, knuuf, yzw]))])


design=[pxep,knuuf,yzw,gzrvlk]
crossing=[gzrvlk]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_3"))

### END
