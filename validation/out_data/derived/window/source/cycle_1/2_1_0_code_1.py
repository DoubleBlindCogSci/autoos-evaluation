from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tmkwf = Factor("tmkwf", ["cjgub","usu","jajoct","jzpu","xepu","simzsx"])
def kobddq(tmkwf):
    return tmkwf[-2] != "jzpu" and tmkwf[-1] == "simzsx"
def tep(tmkwf):
    return tmkwf[-2] == "jzpu" or tmkwf[-1] != "simzsx"
idrfk = Factor("jmyrao", [DerivedLevel("ucfyzp", Window(kobddq, [tmkwf],3,1)), DerivedLevel("pca", Window(tep, [tmkwf],3,1))])
### EXPERIMENT
design=[tmkwf,idrfk]
crossing=[idrfk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END