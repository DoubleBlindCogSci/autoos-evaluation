from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
qmcxwy = Factor("qmcxwy", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
jnubcb = Factor("jnubcb", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
yntx = Factor("yntx", ["bek","citjm","zyg","mvzc","utch","vxcenn","bjdxlv","kudg"])
def kqdgi(qmcxwy, yntx, jnubcb):
     return qmcxwy == yntx
def obds(qmcxwy, yntx, jnubcb):
     return yntx != qmcxwy and qmcxwy == jnubcb
def muki(qmcxwy, yntx, jnubcb):
     return (qmcxwy != yntx) and (qmcxwy != jnubcb)
pmpvu = DerivedLevel("lcas", WithinTrial(kqdgi, [qmcxwy, jnubcb, yntx]))
zaytav = DerivedLevel("xxk", WithinTrial(obds, [qmcxwy, jnubcb, yntx]))
lqfpkr = DerivedLevel("twq", WithinTrial(muki, [qmcxwy, jnubcb, yntx]))
mzk = Factor("iwnx", [pmpvu, zaytav, lqfpkr])

### EXPERIMENT
design=[qmcxwy,jnubcb,yntx,mzk]
crossing=[mzk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END