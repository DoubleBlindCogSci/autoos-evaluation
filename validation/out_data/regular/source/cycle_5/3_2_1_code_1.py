from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dYRB=Factor("TqnSP",['pqgnyBtyR',Level("ZqWUWLTqt@Fggx",1),"AJ)"])
OOV9RYJC=[Level('aHL',4),'XpLoczwKvJY',"spIJDRGSc3"]
FSk8=Factor("5QOKNrcoyYWR",OOV9RYJC)

### EXPERIMENT
design=[dYRB,FSk8]
crossing=[dYRB,FSk8]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END