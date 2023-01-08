from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
txj = Factor("txj", ["qkuf","zbrskh","woqju","njhij","jjba","uotas","uzfvp"])
def is_brx_logc(txj):
    return txj == "zbrskh"
def is_brx_lhavt(txj):
    return txj == "woqju"
def is_brx_wrcs(txj):
    return not (is_brx_logc(txj) or is_brx_lhavt(txj))
brx = Factor("brx", [DerivedLevel("logc", WithinTrial(is_brx_logc, [txj])), DerivedLevel("lhavt", WithinTrial(is_brx_lhavt, [txj])), DerivedLevel("wrcs", WithinTrial(is_brx_wrcs, [txj]))])

design=[txj,brx]
crossing=[brx]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_4"))

### END