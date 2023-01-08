from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qgfryh = Factor("qgfryh", ["bgzts", "rascyb"])
kypx = Factor("kypx", ["tryqxb", "ozpme"])
elf = Factor("elf", ["gqpwr", "oliqg"])

### EXPERIMENT
design=[qgfryh,kypx,elf]
crossing=[[qgfryh,kypx,elf]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_0"))
### END