from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_IhWtp_mZHNk = Factor("}IhWtp$mZHNk", ["xVKcYBsM", "ujqZpsU<", Level("rYi[QKIPh%", 2), "X)jVF;BFQpOfZx", "BdWL9jGhcQq&A"])
__mOqqZEHfJb = Factor("|8mOqqZEHfJb", [" ZOhm", "roW#sIF_", "b$QSXbD", "jlTd7z", "TZs", "tDRYJzM5F6OV6"])


design=[_IhWtp_mZHNk,__mOqqZEHfJb]
crossing=[_IhWtp_mZHNk,__mOqqZEHfJb]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_1"))

### END
