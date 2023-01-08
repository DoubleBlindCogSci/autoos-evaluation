from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
gpvvC7ytisa=Factor("wP!lSU:Jo",[Level('DH0m',1),'HCmbqdwc','LDpdEOjb '])
Lkcc3o=Factor("JGAH",[Level("<lakDe ^]GVW",1),"ZG|yNqHHCj",Level('Ccj6hzwXo',10)])
uqGR=["QzCKug",Level('ausuT5',6),'zHC9vPvYw']
LzjNem9R=Factor("]jInqv9ochDhc",uqGR)

### EXPERIMENT
design=[gpvvC7ytisa,Lkcc3o,LzjNem9R]
crossing=[gpvvC7ytisa,Lkcc3o,LzjNem9R]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_3_0"))
### END