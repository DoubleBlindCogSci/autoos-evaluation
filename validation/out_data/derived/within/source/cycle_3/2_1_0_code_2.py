from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
edve = Factor("edve", ["etus","qyzc","bglrfv","qyrbx","kmbdeo"])
def is_yaly_dbg(edve):
    return edve != "etus"
def is_yaly_rjpq(edve):
    return not is_yaly_dbg(edve)
yaly= Factor("yaly", [DerivedLevel("dbg", WithinTrial(is_yaly_dbg, [edve])), DerivedLevel("rjpq", WithinTrial(is_yaly_rjpq, [edve]))])

design=[edve,yaly]
crossing=[yaly]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_0"))

### END
