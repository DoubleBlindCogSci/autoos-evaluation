from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
LDHmI=Level('wdggRlqel',6)
MrhL37mFUy=Factor("Uybr",["ATLpPSw",LDHmI,"Qyrg","hWjSp",Level("O_ROUCgFYDZ",10),'dowiczkYJJkj(l',Level('t#R',9)])
VFjA5p=Factor("rTwGA",[Level("]&TGB5mxRSCB",4),Level('Dyavv|3C',7),Level("bRuwGpkMq",7),Level("eIkREvKl|Dvr",6),'u><HLRg7ISu',"Kfx}VMlifM"])

### EXPERIMENT
design=[MrhL37mFUy,VFjA5p]
crossing=[MrhL37mFUy,VFjA5p]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_1"))
### END