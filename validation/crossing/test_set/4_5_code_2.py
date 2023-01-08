from sweetpea import *
import os
_dir=os.path.dirname(__file__)
bhrzor = Factor("bhrzor", ["jpqzu", "wqr"])
nhvv = Factor("nhvv", ["jyte", "vgeu"])
rne = Factor("rne", ["ikusc", "oerhlz"])
tpub = Factor("tpub", ["ojhod", "fvdu"])
constraints = []
crossing = [bhrzor, nhvv, rne, tpub]


design=[bhrzor,nhvv,rne,tpub]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_5"))

### END