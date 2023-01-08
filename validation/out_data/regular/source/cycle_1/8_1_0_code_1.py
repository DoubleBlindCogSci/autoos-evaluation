from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pGYZq9k_R="z3o@a"
h_u8UsIbp4=['Exg[AC?ZBF&G',Level('LffPu',3),"k{Bsw:",pGYZq9k_R,Level(")gl",4),"mGH]feSN@E_wZ",'} SXCLk',"EpPGNSOMX|ID&",Level("w3JkLFy!ykO]",8)]
aEs8=Factor('z)T',h_u8UsIbp4)

### EXPERIMENT
design=[aEs8]
crossing=[aEs8]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/8_1_0"))
### END