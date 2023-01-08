from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zpy = Factor("zpy", ["llgvx","iwd","aarjn","rmgm","rmr"])
def tjcc(zpy):
    return zpy[0] == "aarjn" and zpy[-1] != "rmgm"
def lshl(zpy):
    return not (zpy[0] == "aarjn") or not (zpy[0] != "rmgm")
oepk = DerivedLevel("yinzwa", Transition(tjcc, [zpy]))
dgily = DerivedLevel("xmw", Transition(lshl, [zpy]))
arqipi = Factor("dahler", [oepk, dgily])

### EXPERIMENT
design=[zpy,arqipi]
crossing=[arqipi]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END