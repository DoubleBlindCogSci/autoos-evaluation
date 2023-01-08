from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
uLp7=Factor('W]X',[Level('u&j',8),'Irw ]','cP)'])
FCsEM3ljMO=["h}[xOnoj",'nGc',"KxpqG"]
o97A=Factor("*v(uhf",FCsEM3ljMO)

### EXPERIMENT
design=[uLp7,o97A]
crossing=[uLp7,o97A]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END