from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xegutz = Factor("xegutz", ["qzsw","fzvbw","xda","jdmilo","gaalwi","bdmqeu"])
wmxmym = Factor("wmxmym", ["lrwzfp","ysr","qjnpiy","azaopl","use","evg","ppqz"])
def wprj(xegutz, wmxmym):
    return xegutz != "bdmqeu" and wmxmym != "ppqz"
def mbujl(xegutz,wmxmym):
    return xegutz == "bdmqeu" or wmxmym == "ppqz"
zbwucb = DerivedLevel("hhir", WithinTrial(wprj, [xegutz, wmxmym]))
qhepcp = DerivedLevel("ebhy", WithinTrial(mbujl, [xegutz, wmxmym]))
jqocq = Factor("dln", [zbwucb, qhepcp])

### EXPERIMENT
design=[xegutz,wmxmym,jqocq]
crossing=[jqocq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END