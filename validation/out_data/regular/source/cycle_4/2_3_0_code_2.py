from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ELv = Factor("ELv", [Level("chZk0hKWLDK", 3), Level("HNLF", 1)])
Cg__LDfzS__M_ = Factor("Cg}|LDfzS3[M?", [Level("mlNItWvVzGZtfR", 4), Level("vJj(;v", 1)])
Y_ZN_rwKgeZkW = Factor("Y{ZN{rwKgeZkW", ["jdq", "bqbaUVrN]rM", "IyGgMQV{"])

design=[ELv,Cg__LDfzS__M_,Y_ZN_rwKgeZkW]
crossing=[ELv,Cg__LDfzS__M_,Y_ZN_rwKgeZkW]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3_0"))

### END
