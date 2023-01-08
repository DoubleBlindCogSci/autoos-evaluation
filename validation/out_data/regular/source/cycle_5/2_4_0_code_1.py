from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tWkjSJp=['*vEdLnSHq&?MNu',Level('2kFa',1)]
zJuHAHCW=Factor('Lwp(nnRMKq',tWkjSJp)
dyBbr=Factor('GY!',['L9WVAMPvBvuaZ','wy5vkP(aiXm'])
y4Z9AFc=Factor('RrT(Oh',['cuqHR)Z6E2@J',"Dtum4"])
n_0VCm5=Factor('yDe>f',["T^#*bHSDYj",Level('RQ3Qj',1)])

### EXPERIMENT
design=[zJuHAHCW,dyBbr,y4Z9AFc,n_0VCm5]
crossing=[zJuHAHCW,dyBbr,y4Z9AFc,n_0VCm5]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_4_0"))
### END