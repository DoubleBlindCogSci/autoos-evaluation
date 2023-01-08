from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xgtcl = Factor("xgtcl", ["whmbm","jnj","porzs","mph","sbjdi","hbz","ziya"])
def is_fpqvm_fkd(xgtcl):
    return xgtcl[-1] == "sbjdi" or xgtcl[-2] == "ziya"
def is_fpqvm_hnepud(xgtcl):
    return not is_fpqvm_fkd(xgtcl)
fpqvm = Factor("fpqvm", [DerivedLevel("fkd", Window(is_fpqvm_fkd, [xgtcl], 3, 1)), DerivedLevel("hnepud", Window(is_fpqvm_hnepud, [xgtcl], 3, 1))])

design=[xgtcl,fpqvm]
crossing=[fpqvm]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_2"))

### END