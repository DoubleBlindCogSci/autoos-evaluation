from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
opoq= Factor("opoq", ["aonory","ilst","hjph","rsn","ovie","yvqo","fkdakj"])
def is_ddehh_nusuv(opoq):
    return opoq == "rsn"
def is_ddehh_plz(opoq):
    return opoq == "yvqo"
def is_ddehh_hhq(opoq):
    return not (is_ddehh_nusuv(opoq) or is_ddehh_plz(opoq))
ddehh= Factor("ddehh", [DerivedLevel("nusuv", WithinTrial(is_ddehh_nusuv, [opoq])), DerivedLevel("plz", WithinTrial(is_ddehh_plz, [opoq])), DerivedLevel("hhq", WithinTrial(is_ddehh_hhq, [opoq]))])

design=[opoq, ddehh]
crossing=[ddehh]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
