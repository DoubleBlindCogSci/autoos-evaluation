from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ekav= Factor("ekav", ["gdouen","hnajd","ltruym","vbfv","ltssjd"])
dway= Factor("dway", ["gdouen","hnajd","ltruym","vbfv","ltssjd"])
auik= Factor("auik", ["gdouen","hnajd","ltruym","vbfv","ltssjd"])
def is_bfsf_dzw(ekav, dway):
    return ekav[0] == dway[-1]
def is_bfsf_tkf(ekav, dway):
    return not is_bfsf_dzw(ekav, dway)
bfsf= Factor("bfsf", [DerivedLevel("dzw", Transition(is_bfsf_dzw, [ekav, dway])), DerivedLevel("tkf", Transition(is_bfsf_tkf, [ekav, dway]))])

design=[ekav,dway,auik,bfsf]
crossing=[bfsf]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
