from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
a4sra4FI10j=['AmJ(F@ohUpCS]',"p4D","Lw}YpK%","rkHSip"]
bWCIiE=Factor('Vv)lOMVY(',a4sra4FI10j)

### EXPERIMENT
design=[bWCIiE]
crossing=[bWCIiE]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_0"))
### END