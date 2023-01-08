from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xvcj = Factor("xvcj", ["vsw", "khjk"])
xeh = Factor("xeh", ["zawvq", "jpcyk"])
pthpn = Factor("pthpn", ["uvsz", "wcyyg"])

### EXPERIMENT
design=[xvcj,xeh,pthpn]
crossing=[[xvcj,xeh,pthpn],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_1"))
### END