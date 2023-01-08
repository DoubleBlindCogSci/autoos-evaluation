from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
fl6QqKKc=Level('HQHGo@8idP',2)
hZX05z=['bRfDrY','}NtZuYPVKQsZz',fl6QqKKc,Level("kTQcBUmp",3),'UhU']
Zl1fZlq=Factor("emTcasNQXB",hZX05z)

### EXPERIMENT
design=[Zl1fZlq]
crossing=[Zl1fZlq]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_1"))
### END