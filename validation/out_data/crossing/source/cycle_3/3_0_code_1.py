from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vtj = Factor("vtj", ["djrzp", "giar"])
fgqdx = Factor("fgqdx", ["qdwora", "ajipzj"])
mnj = Factor("mnj", ["aiskjo", "qwybt"])
ewol = Factor("ewol", ["sawqek", "goxbv"])
qqdjf = Factor("qqdjf", ["rfkoeh", "brmsf"])
rwg = Factor("rwg", ["gae", "xowm"])
tiug = Factor("tiug", ["rqjbp", "exn"])
fql = Factor("fql", ["ltupt", "oxkq"])

### EXPERIMENT
design=[vtj,fgqdx,mnj,ewol,qqdjf,rwg,tiug,fql]
crossing=[[vtj,fgqdx,mnj],[ewol],[qqdjf,rwg,tiug,fql],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_0"))
### END