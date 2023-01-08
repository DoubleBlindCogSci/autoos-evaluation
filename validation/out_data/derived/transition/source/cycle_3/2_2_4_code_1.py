from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
wvbcpr = Factor("wvbcpr", ["tvu","sibqd","zngsmx","vyhnva","cuye"])
gojw = Factor("gojw", ["eye","bpk","imevr","xcdji","boz","rjceq","huhrj"])
def xqoux(wvbcpr, gojw):
    return wvbcpr[0] == "cuye" or gojw[-1] != "eye"
def gzmsqh(wvbcpr,gojw):
    return not (wvbcpr[0] == "cuye") and gojw[-1] == "eye"
sqjg = DerivedLevel("feeiiy", Transition(xqoux, [wvbcpr, gojw]))
yyyrcf = DerivedLevel("oudod", Transition(gzmsqh, [wvbcpr, gojw]))
jltit = Factor("xpvgza", [sqjg, yyyrcf])

### EXPERIMENT
design=[wvbcpr,gojw,jltit]
crossing=[jltit]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_4"))
### END