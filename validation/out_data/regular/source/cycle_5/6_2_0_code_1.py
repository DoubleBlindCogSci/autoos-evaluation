from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vJZVQMrt=["Q&E$mvGpGg",'rsdDm0t',"Qam",'Jis',"ANi","EIu"]
QG2QPo_uI=Factor('_)QDVOrqBg',vJZVQMrt)
JD5fJ=Factor('t{sywPp',['{eQ',")bMciYGc&Bre",'olkYs$oeP',Level("K7YNvthvfBE>",3),'zCLQzJ<E$J','yzn[LG'])

### EXPERIMENT
design=[QG2QPo_uI,JD5fJ]
crossing=[QG2QPo_uI,JD5fJ]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_0"))
### END