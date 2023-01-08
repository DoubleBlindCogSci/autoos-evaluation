from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xegutz = Factor("xegutz", ["qzsw","fzvbw","xda","jdmilo","gaalwi","bdmqeu"])
wmxmym = Factor("wmxmym", ["lrwzfp","ysr","qjnpiy","azaopl","use","evg","ppqz"])
def is_dln_hhir(xegutz, wmxmym):
    return xegutz != "bdmqeu" and wmxmym != "ppqz"
def is_dln_ebhy(xegutz, wmxmym):
    return not is_dln_hhir(xegutz, wmxmym)
dln= Factor("dln", [DerivedLevel("hhir", WithinTrial(is_dln_hhir, [xegutz, wmxmym])), DerivedLevel("ebhy", WithinTrial(is_dln_ebhy, [xegutz, wmxmym]))])

design=[xegutz,wmxmym,dln]
crossing=[dln]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
