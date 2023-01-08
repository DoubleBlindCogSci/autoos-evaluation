from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ynxmRT=Factor('v_J',['bZmcE@I',"dLlbWhO;",'HHZnXj','JI%%REE',"ZoJ","WOCPPJJl*YLWJ$","rDsKX~hRgl","DWOBAyAQ",Level("X8wvcPgdMeVX",10)])

### EXPERIMENT
design=[ynxmRT]
crossing=[ynxmRT]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/9_1_1"))
### END