from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fxc = Factor("fxc", ["orpjc","ssfjo","xmpi","erdht","awmuij"])
def is_bovds_micnu(fxc):
    return fxc[0] == "xmpi" or fxc[-3] != "ssfjo"
def is_bovds_zcq(fxc):
    return not is_bovds_micnu(fxc)
bovds= Factor("bovds", [DerivedLevel("micnu", Window(is_bovds_micnu, [fxc], 4, 1)), DerivedLevel("zcq", Window(is_bovds_zcq, [fxc], 4, 1))])

design=[fxc,bovds]
crossing=[bovds]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_3"))

### END
