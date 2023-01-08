from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
flYUwZ=Factor("]bRxu?nA!A",['yh#SkZ$I',Level('Y%ou~IceHMu:Br',8),"SeBL","l}gPXP0i"])
lTq5=Factor('BBK]lP@nOHZ@Y',["FcPaPVVD;BuOtQ",'(nweqHF(hl',Level('GMJiBe',9),"wI7n6filLu"])

### EXPERIMENT
design=[flYUwZ,lTq5]
crossing=[flYUwZ,lTq5]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_2_0"))
### END