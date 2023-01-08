from sweetpea import *
import os
_dir=os.path.dirname(__file__)
xvcj = Factor("xvcj", ["vsw", "khjk"])
xeh = Factor("xeh", ["zawvq", "jpcyk"])
pthpn = Factor("pthpn", ["uvsz", "wcyyg"])
constraints = []
crossing = [xvcj, xeh, pthpn]


design=[xvcj,xeh,pthpn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_1"))

### END