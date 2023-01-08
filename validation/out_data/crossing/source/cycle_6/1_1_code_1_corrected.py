from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
btxs = Factor("btxs", ["ecflws", "nwotye"])
tidm = Factor("tidm", ["dhgne", "gya"])

### EXPERIMENT
design=[btxs,tidm]
crossing = [[btxs,tidm],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_1"))
### END
