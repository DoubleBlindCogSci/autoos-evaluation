from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gcM2dzT1S=Factor("kMXgAq",['RZzjWytRXBYKMC','gkk0TGK(GvI',"aAQXO_",Level('z!J}',2),"N6esUhr[6","hK{k7N",'TxGFPUBhBx',"vpulRruR|Kih",Level('l;riM',3)])

### EXPERIMENT
design=[gcM2dzT1S]
crossing=[gcM2dzT1S]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_1_0"))
### END