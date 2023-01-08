from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
CV3I=Factor('ZdkRbRp:P',[Level('Fb7dSvHvCg Ga',8),'Eiy]ly',Level('}3QL',3)])
vG8op_mxAt=Factor('p1KMSdDk',[Level('HONKDt',3),'OHitE','YU f'])
HsP2k3vmS=["5zJZXXSWn",Level('%J7MvI3',9),"TspfX"]
PXmk_=Factor('La^0wTd^4iQ',HsP2k3vmS)

### EXPERIMENT
design=[CV3I,vG8op_mxAt,PXmk_]
crossing=[CV3I,vG8op_mxAt,PXmk_]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_1"))
### END