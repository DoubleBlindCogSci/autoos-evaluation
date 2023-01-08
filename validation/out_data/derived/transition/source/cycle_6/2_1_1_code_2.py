from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zpy = Factor("zpy", ["llgvx","iwd","aarjn","rmgm","rmr"])
def is_dahler_yinzwa(zpy):
    return zpy[0] == "aarjn" and zpy[-1] != "rmgm"
def is_dahler_xmw(zpy):
    return not is_dahler_yinzwa(zpy)
dahler = Factor("dahler", [DerivedLevel("yinzwa", Transition(is_dahler_yinzwa, [zpy])), DerivedLevel("xmw", Transition(is_dahler_xmw, [zpy]))])

design=[zpy,dahler]
crossing=[dahler]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_1"))

### END