from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vDKtU=Factor('xTOwUCLvJCZYec',["MckQxHCIqKTMh","auQp"])
zf_9EEK=["JBT{xb",'dvdy}&ZA']
jZZ2=Factor('EF<p|&FYX',zf_9EEK)
oLOLs6SLJm=['RkpdX',"vx?B"]
ZD0WAS=Factor('IF}njruktyV',oLOLs6SLJm)

### EXPERIMENT
design=[vDKtU,jZZ2,ZD0WAS]
crossing=[vDKtU,jZZ2,ZD0WAS]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_1"))
### END