from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
edve = Factor("edve", ["etus","qyzc","bglrfv","qyrbx","kmbdeo"])
def fjuw(edve):
    return edve != "etus"
def bdvtak(edve):
    return not fjuw(edve)
bdo = Factor("yaly", [DerivedLevel("dbg", WithinTrial(fjuw, [edve])), DerivedLevel("rjpq", WithinTrial(bdvtak, [edve]))])
### EXPERIMENT
design=[edve,bdo]
crossing=[bdo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END