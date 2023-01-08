from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OOyj=Factor("FcUlGzASLNKP(v",[Level('Zo$b<?LHZYsw',7),'BERk[mgcl',Level("mcmW!~OZqd",8),Level('RHkFRhKFB',2),'tdHW#Ug7mCJTF'])
wddC51=Factor('aG9iGruiEpi',["{ 1N",'eNhfUe MH4gx',"W:L#SLKyD df",Level("HU0PWfKY|)",10),'qiRL'])
DKKZQXmZZH=Factor("b]arlTT",[Level('hR%q',3),Level('9Os_',7),'5U|SQ',Level("Gxu",5),'fnaZmSKA6'])

### EXPERIMENT
design=[OOyj,wddC51,DKKZQXmZZH]
crossing=[OOyj,wddC51,DKKZQXmZZH]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_3_0"))
### END