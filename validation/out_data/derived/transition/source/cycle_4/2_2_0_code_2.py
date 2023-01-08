from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zbl = Factor("zbl", ["ecmf","kdv","ymd","vpiv","wfcfy"])
jvc = Factor("jvc", ["heic","flb","pgw","nosjfm","mcbage","sdixdv"])
def is_tnq_scp(zbl, jvc):
    return zbl[0] != "vpiv" and jvc[0] != "heic"
def is_tnq_kelr(zbl, jvc):
    return not is_tnq_scp(zbl, jvc)
tnq= Factor("tnq", [DerivedLevel("scp", Transition(is_tnq_scp, [zbl, jvc])), DerivedLevel("kelr", Transition(is_tnq_kelr, [zbl, jvc]))])

design=[zbl,jvc,tnq]
crossing=[tnq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END