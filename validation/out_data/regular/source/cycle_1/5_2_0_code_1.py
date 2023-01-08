from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
Ak6TKQz1wz=Factor('aFFrDTJF~',["NCeyfqWILr5RzI",Level("YH%njwHgJe",5),'pPr08Ddvqy','DM?fq Bzq',"DpD|IK Boe"])
UjhTMAufZVB=Factor("KJgiTHr7lW",['}LY',Level('chk>mOUZsDPlO',3),Level(']~@FmCBJsA',8),Level('RUDwvZ?',8),'AQ}RRYJf2)<Uje'])

### EXPERIMENT
design=[Ak6TKQz1wz,UjhTMAufZVB]
crossing=[Ak6TKQz1wz,UjhTMAufZVB]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/5_2_0"))
### END