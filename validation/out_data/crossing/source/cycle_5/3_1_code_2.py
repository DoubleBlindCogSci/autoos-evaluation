from sweetpea import *
import os
_dir=os.path.dirname(__file__)
uugpxi = Factor("uugpxi", ["nbzjzu", "xozpwp"])
qonvzg = Factor("qonvzg", ["acln", "fhz"])
ulqva = Factor("ulqva", ["wrw", "csg"])
nsc = Factor("nsc", ["wqfa", "vote"])
tznmq = Factor("tznmq", ["oay", "frlzt"])
mdbny = Factor("mdbny", ["gesf", "ifdp"])
dyrgky = Factor("dyrgky", ["ceckb", "vbxxz"])
dtj = Factor("dtj", ["exi", "tgi"])
labfev = Factor("labfev", ["xdrh", "fco"])
constraints = []
crossing = [[uugpxi, qonvzg], [ulqva, nsc, tznmq, mdbny], [dyrgky, dtj, labfev]]


design=[uugpxi,qonvzg,ulqva,nsc,tznmq,mdbny,dyrgky,dtj,labfev]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END