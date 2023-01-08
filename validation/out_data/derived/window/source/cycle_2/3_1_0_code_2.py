from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tdnox= Factor("tdnox", ["kqpv","hrotnx","dasrau","ybtjiu","hulttu","qacp"])
def is_tmvjq_uto(tdnox):
    return tdnox[-2] == "hrotnx" and tdnox[-3] != "hrotnx"
def is_tmvjq_ifontz(tdnox):
    return tdnox[-2] != "hrotnx" and tdnox[-3] == "qacp"
def is_tmvjq_ntqamr(tdnox):
    return tdnox[-2] != "hrotnx" and tdnox[-3] != "qacp"
tmvjq= Factor("tmvjq", [DerivedLevel("uto", Window(is_tmvjq_uto, [tdnox], 4, 1)), DerivedLevel("ifontz", Window(is_tmvjq_ifontz, [tdnox], 4, 1)), DerivedLevel("ntqamr", Window(is_tmvjq_ntqamr, [tdnox], 4, 1))])

design=[tdnox,tmvjq]
crossing=[tmvjq]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_0"))

### END
