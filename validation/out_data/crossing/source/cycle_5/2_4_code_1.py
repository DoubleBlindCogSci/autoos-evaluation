from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
hlexth = Factor("hlexth", ["dmat", "jdtlrj"])
nvtt = Factor("nvtt", ["tvlj", "kgim"])
ndetb = Factor("ndetb", ["vqzu", "jsxb"])
couad = Factor("couad", ["vockcr", "pyf"])

### EXPERIMENT
design=[hlexth,nvtt,ndetb,couad]
crossing=[[hlexth],[nvtt,ndetb,couad],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_4"))
### END