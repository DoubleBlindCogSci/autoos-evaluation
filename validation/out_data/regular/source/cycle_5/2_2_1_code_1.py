from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
AhkO=Factor("Ihj",["SZcP$q7T3E4Xkt",'q4(peIyBCDBe'])
Fh_JW=Factor("mNPT[!Lq2x~",["aPoSYR2ehnve","BSF"])

### EXPERIMENT
design=[AhkO,Fh_JW]
crossing=[AhkO,Fh_JW]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_1"))
### END