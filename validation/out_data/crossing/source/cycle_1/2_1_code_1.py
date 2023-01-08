from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lgpxu = Factor("lgpxu", ["aikdrw", "cttb"])
rak = Factor("rak", ["gqya", "ubz"])
nyrh = Factor("nyrh", ["eqzyq", "mjpkrd"])

### EXPERIMENT
design=[lgpxu,rak,nyrh]
crossing=[[lgpxu],[rak,nyrh],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1"))
### END