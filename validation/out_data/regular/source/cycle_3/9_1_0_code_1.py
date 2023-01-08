from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vQJ2i5ae=Factor("IBDVkH",["vvp","MO<Y:2w9&L",'2uZqVCxLgF',"piWiEwOAGus",Level("yOXTOW",3),"xqO",Level("eOGELHT0npm",2),Level('u2n:lR',9),Level("YcDBOFK",7)])

### EXPERIMENT
design=[vQJ2i5ae]
crossing=[vQJ2i5ae]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_1_0"))
### END