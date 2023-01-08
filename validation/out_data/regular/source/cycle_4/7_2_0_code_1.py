from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aCfhoIk=Factor("jHDCE",["InST:kxae",Level('MfLUPxpGszDb',4),'FtKxNdDtOn8dri','KOyK',"InZ|",'dhNtFzbwjDM}O','EvEKTf'])
L3uny=["(wvqjawd*mh",'ElzyZldi|FZyZ','Cs@','|_PKersD](jwpP',Level("kjgUIAlozFRoyt",1),Level("XeaJh?K",3),";laEhTQPABNh"]
uDiL=Factor('LztfSJW2H?WQy',L3uny)

### EXPERIMENT
design=[aCfhoIk,uDiL]
crossing=[aCfhoIk,uDiL]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_0"))
### END