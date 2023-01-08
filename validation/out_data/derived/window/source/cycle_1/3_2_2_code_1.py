from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mfz = Factor("mfz", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
jtrvnd = Factor("jtrvnd", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
zrs = Factor("zrs", ["vnln","hxzpb","zurgyz","jije","ccht","ahonws"])
def pit(mfz, zrs, jtrvnd):
     return zrs[-2] == mfz[-1]
def wgt(mfz, zrs, jtrvnd):
     return zrs[-2] != mfz[-1] and jtrvnd[-1] == mfz[-2]
def lmzmt(mfz, zrs, jtrvnd):
     return (not pit(mfz, zrs, jtrvnd)) and (not mfz[-2] == jtrvnd[-1])
rmabm = DerivedLevel("rap", Window(pit, [mfz, jtrvnd, zrs],3,1))
zbswp = DerivedLevel("gpksp", Window(wgt, [mfz, jtrvnd, zrs],3,1))
babh = DerivedLevel("xqjhvf", Window(lmzmt, [mfz, jtrvnd, zrs],3,1))
oudg = Factor("yaehve", [rmabm, zbswp, babh])

### EXPERIMENT
design=[mfz,jtrvnd,zrs,oudg]
crossing=[oudg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END