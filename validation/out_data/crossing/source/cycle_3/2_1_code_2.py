from sweetpea import *
import os
_dir=os.path.dirname(__file__)
zhktq = Factor("zhktq", ["wqbv", "nxf"])
fscf = Factor("fscf", ["yaph", "the"])
yvnnet = Factor("yvnnet", ["yog", "pklwli"])
rqqp = Factor("rqqp", ["bdbua", "quk"])
ncl = Factor("ncl", ["safafm", "vulq"])
hyktlk = Factor("hyktlk", ["jpstxk", "qhhbr"])
constraints = []
crossing = [[zhktq, fscf], [yvnnet, rqqp, ncl, hyktlk]]


design=[zhktq,fscf,yvnnet,rqqp,ncl,hyktlk]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1"))

### END