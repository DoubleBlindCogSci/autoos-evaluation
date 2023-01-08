from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
B5IuHVCjn=Factor('K4*YSnO',["qh7HlEdQ>X^So","rAPZ^pks2",":tdvuIdM_NIeAo","dXKX ","pAr","[8r","lgulPGcnZt_tnS"])
zTbyP=Factor('W<(pRbUvx',['XX^vopHE',"!ki9ohJS@aI",'nMgiVw',"qWpxsjddz","sbNz",'gKCBwAT',"wzXIIJx"])

### EXPERIMENT
design=[B5IuHVCjn,zTbyP]
crossing=[B5IuHVCjn,zTbyP]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2_0"))
### END