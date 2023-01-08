from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
fpmp = Factor("fpmp", ["izg","ozu","hqozcd","oviwqe","wmer"])
ncvlo = Factor("ncvlo", ["jiad","noxk","pqfqdr","imtdk","hrnm","cdjfyd"])
def tpqk(fpmp, ncvlo):
    return fpmp[0] != "ozu" and ncvlo[-1] != "noxk"
def dwynwd(fpmp,ncvlo):
    return fpmp[0] == "ozu" or ncvlo[-1] == "noxk"
mvj = Factor("hocpea", [DerivedLevel("onqun", Transition(tpqk, [fpmp, ncvlo])), DerivedLevel("vgarrq", Transition(dwynwd, [fpmp, ncvlo]))])
### EXPERIMENT
design=[fpmp,ncvlo,mvj]
crossing=[mvj]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END