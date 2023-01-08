from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vhuevy = Factor("vhuevy", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
ddn = Factor("ddn", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
cfsfa = Factor("cfsfa", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
def eeetnn(vhuevy, cfsfa, ddn):
    return vhuevy != cfsfa
def cyy(vhuevy, cfsfa, ddn):
    return vhuevy == cfsfa
his = DerivedLevel("ilpaj", WithinTrial(eeetnn, [vhuevy, ddn, cfsfa]))
nyl = DerivedLevel("jnoqn", WithinTrial(cyy, [vhuevy, ddn, cfsfa]))
jawdy = Factor("zkkck", [his, nyl])

### EXPERIMENT
design=[vhuevy,ddn,cfsfa,jawdy]
crossing=[jawdy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END