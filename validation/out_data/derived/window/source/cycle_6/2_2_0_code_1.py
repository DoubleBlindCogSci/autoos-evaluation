from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
orv = Factor("orv", ["ecf","ctx","ydzol","fry","tmjvn"])
umaucr = Factor("umaucr", ["ecf","ctx","ydzol","fry","tmjvn"])
fdcldf = Factor("fdcldf", ["ecf","ctx","ydzol","fry","tmjvn"])
def qcyk(orv, umaucr, fdcldf):
    return orv[-1] == umaucr[0] and orv[0] == fdcldf[-1]
def lwyy(orv, umaucr, fdcldf):
    return orv[-1] != umaucr[0] or orv[0] != fdcldf[-1]
iuc = DerivedLevel("ayso", Window(qcyk, [orv, umaucr, fdcldf],2,1))
fznamu = DerivedLevel("asl", Window(lwyy, [orv, umaucr, fdcldf],2,1))
ppj = Factor("nlgc", [iuc, fznamu])

### EXPERIMENT
design=[orv,umaucr,fdcldf,ppj]
crossing=[ppj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END