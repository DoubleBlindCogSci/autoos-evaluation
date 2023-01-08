from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
oCh1IwRb=Factor('$XkYk',[Level("XuaQS$gQZ",6),'Pz!prPZ*j po','uQ~WM}%poZCY',"2dAGZcyq]MX",Level("twP",4),'KUXy XBS',Level('aofcpBsALYE',3),'wiMOx7:'])
B7kgPkz2B='%YH'
ySJPc_Imh=Factor('BpAj',[Level('sBeOqqMlr}x',6),Level('~VoK',4),'YCW',Level('qynojic',4),B7kgPkz2B,"XAFx",'YiY{M;n_cZ',Level("BvMx hh$w_[",6),"dwczRb9"])

### EXPERIMENT
design=[oCh1IwRb,ySJPc_Imh]
crossing=[oCh1IwRb,ySJPc_Imh]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_1"))
### END