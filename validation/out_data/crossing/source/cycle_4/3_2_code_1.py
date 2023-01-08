from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
iazoh = Factor("iazoh", ["djo", "dcxsf"])
scbb = Factor("scbb", ["nbx", "uik"])
gpdrba = Factor("gpdrba", ["tgl", "qww"])
hpzmb = Factor("hpzmb", ["tyix", "pku"])
xepyfz = Factor("xepyfz", ["vibig", "biloce"])

### EXPERIMENT
design=[iazoh,scbb,gpdrba,hpzmb,xepyfz]
crossing=[[iazoh],[scbb,gpdrba],[hpzmb,xepyfz],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END