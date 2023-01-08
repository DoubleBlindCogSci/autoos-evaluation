from sweetpea import *
import os
_dir=os.path.dirname(__file__)
zkem = Factor("zkem", ["jclg", "ctf"])
cnsdbq = Factor("cnsdbq", ["wsxta", "nsw"])
constraints = []
crossing = [zkem, cnsdbq]


design=[zkem,cnsdbq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_6"))

### END