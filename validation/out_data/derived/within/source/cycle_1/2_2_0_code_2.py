from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vhuevy= Factor("vhuevy", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
ddn= Factor("ddn", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
cfsfa= Factor("cfsfa", ["nlnmo","hgjot","axst","cgaogw","fhit","fhay","bxph"])
def is_zkkck_ilpaj(vhuevy, ddn, cfsfa):
    return vhuevy != cfsfa
def is_zkkck_jnoqn(vhuevy, ddn, cfsfa):
    return not is_zkkck_ilpaj(vhuevy, ddn, cfsfa)
zkkck= Factor("zkkck", [DerivedLevel("ilpaj", WithinTrial(is_zkkck_ilpaj, [vhuevy, ddn, cfsfa])), DerivedLevel("jnoqn", WithinTrial(is_zkkck_jnoqn, [vhuevy, ddn, cfsfa]))])

design=[vhuevy,ddn,cfsfa,zkkck]
crossing=[zkkck]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
