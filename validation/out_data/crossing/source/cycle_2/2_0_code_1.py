from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dgstb = Factor("dgstb", ["wwhqlf", "brwcn"])
wsexn = Factor("wsexn", ["agoq", "sjxzy"])
xmclt = Factor("xmclt", ["linvy", "ndt"])
srl = Factor("srl", ["nxge", "rrnr"])
fvl = Factor("fvl", ["hiki", "affie"])

### EXPERIMENT
design=[dgstb,wsexn,xmclt,srl,fvl]
crossing=[[dgstb,wsexn,xmclt],[srl,fvl],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_0"))
### END