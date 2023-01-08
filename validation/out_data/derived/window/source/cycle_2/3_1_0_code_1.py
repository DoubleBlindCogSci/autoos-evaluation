from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
tdnox = Factor("tdnox", ["kqpv","hrotnx","dasrau","ybtjiu","hulttu","qacp"])
def wry(tdnox):
     return "hrotnx" == tdnox[-2] and not tdnox[-3] == "hrotnx"
def mwkbj(tdnox):
     return not "hrotnx" == tdnox[-2] and  "qacp" == tdnox[-3]
def nkyc(tdnox):
     return (not tdnox[-2] == "hrotnx") and (tdnox[-3] != "qacp")
xpon = Factor("tmvjq", [DerivedLevel("uto", Window(wry, [tdnox],4,1)), DerivedLevel("ifontz", Window(mwkbj, [tdnox],4,1)),DerivedLevel("ntqamr", Window(nkyc, [tdnox],4,1))])
### EXPERIMENT
design=[tdnox,xpon]
crossing=[xpon]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END