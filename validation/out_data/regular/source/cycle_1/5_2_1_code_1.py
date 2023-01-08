from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cQwDUL7pH=Factor('NsqqYlavrf1IlZ',["I%JSJ",'pZX',')RVRs',Level('a9UAMJLkr',2),"sSPdU{WU"])
U3_RWzK1S7=[Level("0UqUEcb",10),'DWirHPcUJVPR!a','YozSOPeMjrX',"arfwGArd","u k~De!X H"]
aIs6k=Factor(';yrmvG',U3_RWzK1S7)

### EXPERIMENT
design=[cQwDUL7pH,aIs6k]
crossing=[cQwDUL7pH,aIs6k]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_2_1"))
### END