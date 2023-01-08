from sweetpea import *
import os
_dir=os.path.dirname(__file__)
dgstb = Factor("dgstb", ["wwhqlf", "brwcn"])
wsexn = Factor("wsexn", ["agoq", "sjxzy"])
xmclt = Factor("xmclt", ["linvy", "ndt"])
srl = Factor("srl", ["nxge", "rrnr"])
fvl = Factor("fvl", ["hiki", "affie"])
constraints = []
crossing = [[dgstb, wsexn, xmclt], [srl, fvl]]


design=[dgstb,wsexn,xmclt,srl,fvl]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_0"))

### END