from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IsDbeqyJ7Hy=Factor('wFEZE#WUQ^t',[Level("S9Gz",9),"]uxfmS3bj}6e8J","ryhLbZLomRXrRH","S1UcMomU_r",Level("upmMsKYZ62P",1),'JFfOH0?yxI ',"WXXP",'dsQ7ezis~j'])
uTfi=["2URpZLt",Level("L7eW79tbVind",4),Level('gCXjuKd7EvLFDA',6),'9zTxCzUQSQd#q',"EEMHqfpV]","EgKs)uVRZmNws",'FanE','sN4tdjli]']
euzPM=Factor("QfmIuVqDqzptL",uTfi)

### EXPERIMENT
design=[IsDbeqyJ7Hy,euzPM]
crossing=[IsDbeqyJ7Hy,euzPM]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_2_0"))
### END