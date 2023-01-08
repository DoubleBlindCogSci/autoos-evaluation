from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hlexth = Factor("hlexth", ["dmat", "jdtlrj"])
nvtt = Factor("nvtt", ["tvlj", "kgim"])
ndetb = Factor("ndetb", ["vqzu", "jsxb"])
couad = Factor("couad", ["vockcr", "pyf"])
constraints = []
crossing = [hlexth, nvtt, ndetb, couad]


design=[hlexth,nvtt,ndetb,couad]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_4"))

### END