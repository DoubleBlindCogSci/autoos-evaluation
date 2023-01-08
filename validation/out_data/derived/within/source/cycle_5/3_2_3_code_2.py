from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qnydp = Factor("qnydp", ["nervs","yui","exbykd","ofjg","pnkdfj","kpip","gmy","jsno"])
wayn = Factor("wayn", ["ljxc","hdyo","engxux","atdyxi","dtuvgm","zjhnyn","tvb","rinri"])
def is_ltd_xqosw(qnydp, wayn):
    return qnydp == "ofjg"
def is_ltd_eortzq(qnydp, wayn):
    return qnydp != "ofjg" and wayn == "tvb"
def is_ltd_czvpgj(qnydp, wayn):
    return not (is_ltd_xqosw(qnydp, wayn) or is_ltd_eortzq(qnydp, wayn))
ltd = Factor("ltd", [DerivedLevel("xqosw", WithinTrial(is_ltd_xqosw, [qnydp, wayn])), DerivedLevel("eortzq", WithinTrial(is_ltd_eortzq, [qnydp, wayn])), DerivedLevel("czvpgj", WithinTrial(is_ltd_czvpgj, [qnydp, wayn]))])

design=[qnydp,wayn,ltd]
crossing=[ltd]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END