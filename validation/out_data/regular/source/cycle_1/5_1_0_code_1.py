from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hiOyccHz4=Level('mQ30',4)
fk0MsQ=[hiOyccHz4,"eL3ohDXn",";CURDohH","Z$Pnf^",Level('A]8NtVkkCZ',2),Level("3rFK^E(vzT",7)]
d6hMYl=Factor('kzyW',fk0MsQ)

### EXPERIMENT
design=[d6hMYl]
crossing=[d6hMYl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_1_0"))
### END