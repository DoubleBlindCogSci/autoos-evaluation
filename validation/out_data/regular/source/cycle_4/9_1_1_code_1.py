from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
b0xbeAU=Factor("midm:Vqq]J$yA",['oLTaL}TYj',"NbJhVeQAb8&","v%YCZMUE","HCoMJGXru[6py",'(XmMLY(DNWscnd','aVCRmRBC','i!MP{u_MmV5','nfdOSlLEysUx8|',"Oj N9Ljae}$BD"])

### EXPERIMENT
design=[b0xbeAU]
crossing=[b0xbeAU]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/9_1_1"))
### END