from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zkem = Factor("zkem", ["jclg", "ctf"])
cnsdbq = Factor("cnsdbq", ["wsxta", "nsw"])

### EXPERIMENT
design=[zkem,cnsdbq]
crossing=[[zkem,cnsdbq]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_6"))
### END