from sweetpea import *
import os
_dir=os.path.dirname(__file__)
lgpxu = Factor("lgpxu", ["aikdrw", "cttb"])
rak = Factor("rak", ["gqya", "ubz"])
nyrh = Factor("nyrh", ["eqzyq", "mjpkrd"])
constraints = []
crossing = [[lgpxu, rak], [rak, nyrh]]


design=[lgpxu,rak,nyrh]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END