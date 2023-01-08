from sweetpea import *
import os
_dir=os.path.dirname(__file__)
qgfryh = Factor("qgfryh", ["bgzts", "rascyb"])
kypx = Factor("kypx", ["tryqxb", "ozpme"])
elf = Factor("elf", ["gqpwr", "oliqg"])
constraints = []
crossing = [qgfryh, kypx, elf]


design=[qgfryh,kypx,elf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_0"))

### END