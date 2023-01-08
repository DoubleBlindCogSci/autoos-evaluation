from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bhrzor = Factor("bhrzor", ["jpqzu", "wqr"])
nhvv = Factor("nhvv", ["jyte", "vgeu"])
rne = Factor("rne", ["ikusc", "oerhlz"])
tpub = Factor("tpub", ["ojhod", "fvdu"])

### EXPERIMENT
design=[bhrzor,nhvv,rne,tpub]
crossing=[[bhrzor,nhvv,rne,tpub]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_5"))
### END