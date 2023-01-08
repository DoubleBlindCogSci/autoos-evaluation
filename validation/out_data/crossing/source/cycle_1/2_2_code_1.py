from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jus = Factor("jus", ["pcavs", "ywwli"])
wydb = Factor("wydb", ["clvbm", "hgko"])
tbdiy = Factor("tbdiy", ["fkisfx", "ivzs"])

### EXPERIMENT
design=[jus,wydb,tbdiy]
crossing=[[jus,wydb],[tbdiy],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2"))
### END