from sweetpea import *
import os
_dir=os.path.dirname(__file__)
btxs = Factor("btxs", ["ecflws", "nwotye"])
tidm = Factor("tidm", ["dhgne", "gya"])
constraints = []
crossing = [[btxs, tidm],]


design=[btxs,tidm]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_1"))

### END
