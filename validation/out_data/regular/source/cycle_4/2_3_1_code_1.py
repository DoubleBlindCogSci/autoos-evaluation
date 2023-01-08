from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
X23o='T$8z%QZiu7['
VqsX=[';Sn$P0(OjN&u7!',Level('JngTJvF[Q<w',2),X23o]
DdZhrBJgo=Factor("kj8bFlzzZxBUWN",VqsX)
cPi2CmmPC=Factor("&eKIIcWPARN%",["E&XhX}ucj;",'{trZJ(zWTu'])
lWrn1=Factor("iDRw",['aoLSwy_mvY0HAg','MAQD[8hhm'])

### EXPERIMENT
design=[DdZhrBJgo,cPi2CmmPC,lWrn1]
crossing=[DdZhrBJgo,cPi2CmmPC,lWrn1]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3_1"))
### END