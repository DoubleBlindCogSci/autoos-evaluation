from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xbsjPGV=[Level('EftQj}iZ',1),Level('*hY^VVAWMpGB',7)]
oXuFNfQ=Factor("k%ao PgTEM",xbsjPGV)

### EXPERIMENT
design=[oXuFNfQ]
crossing=[oXuFNfQ]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_0"))
### END