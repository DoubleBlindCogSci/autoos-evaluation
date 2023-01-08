from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
nUp4=["jyxr4n",Level("KnydF5]Vw#N",4)]
JOPON54N8f=Factor("hbNsD9ILs",nUp4)

### EXPERIMENT
design=[JOPON54N8f]
crossing=[JOPON54N8f]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END