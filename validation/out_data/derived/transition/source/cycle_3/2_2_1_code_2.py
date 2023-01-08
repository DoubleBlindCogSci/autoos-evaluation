from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fpmp = Factor("fpmp", ["izg","ozu","hqozcd","oviwqe","wmer"])
ncvlo = Factor("ncvlo", ["jiad","noxk","pqfqdr","imtdk","hrnm","cdjfyd"])
def is_hocpea_onqun(fpmp, ncvlo):
    return fpmp[0] != "ozu" and ncvlo[-1] != "noxk"
def is_hocpea_vgarrq(fpmp, ncvlo):
    return not is_hocpea_onqun(fpmp, ncvlo)
hocpea= Factor("hocpea", [DerivedLevel("onqun", Transition(is_hocpea_onqun, [fpmp, ncvlo])), DerivedLevel("vgarrq", Transition(is_hocpea_vgarrq, [fpmp, ncvlo]))])

design=[fpmp,ncvlo,hocpea]
crossing=[hocpea]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_1"))

### END
