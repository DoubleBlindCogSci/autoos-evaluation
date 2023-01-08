from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xtf = Factor("xtf", ["cbi", "xsk"])
vcblky = Factor("vcblky", ["skpvas", "ihho"])
blv = Factor("blv", ["ypksjf", "ilui"])
fnhazr = Factor("fnhazr", ["qnv", "bdhyn"])
isjn = Factor("isjn", ["gqsdeg", "idk"])
lyls = Factor("lyls", ["veq", "hvdnc"])
idw = Factor("idw", ["frbr", "lapno"])

### EXPERIMENT
design=[xtf,vcblky,blv,fnhazr,isjn,lyls,idw]
crossing=[[xtf,vcblky,blv,fnhazr,isjn,lyls,idw]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/7_2"))
### END