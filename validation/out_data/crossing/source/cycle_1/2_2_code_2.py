from sweetpea import *
import os
_dir=os.path.dirname(__file__)
jus = Factor("jus", ["pcavs", "ywwli"])
wydb = Factor("wydb", ["clvbm", "hgko"])
tbdiy = Factor("tbdiy", ["fkisfx", "ivzs"])
constraints = []
crossing = [[jus, wydb], [tbdiy]]


design=[jus,wydb,tbdiy]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2"))

### END