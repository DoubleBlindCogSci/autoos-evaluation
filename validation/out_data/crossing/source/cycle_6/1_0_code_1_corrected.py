from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qsfoh = Factor("qsfoh", ["oaeu", "wkgkc"])
bmu = Factor("bmu", ["qskrq", "vyqjli"])

### EXPERIMENT
design=[qsfoh,bmu]
crossing = [[qsfoh,bmu],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_0"))
### END
