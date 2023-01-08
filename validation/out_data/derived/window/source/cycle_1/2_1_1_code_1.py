from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vrh = Factor("vrh", ["omipuk","isgp","ycd","vynlqp","lmylt"])
def som(vrh):
    return vrh[-3] == "isgp" and vrh[0] == "omipuk"
def szkum(vrh):
    return vrh[-3] != "isgp" or not (vrh[0] == "omipuk")
pju = Factor("xtq", [DerivedLevel("jhzoqx", Window(som, [vrh],4,1)), DerivedLevel("lhbwh", Window(szkum, [vrh],4,1))])
### EXPERIMENT
design=[vrh,pju]
crossing=[pju]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_1"))
### END