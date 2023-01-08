from sweetpea import *
import os
_dir=os.path.dirname(__file__)
vjrzs = Factor("vjrzs", ["ymzbup", "jrtvj"])
gzcohl = Factor("gzcohl", ["yrrch", "kyrlkh"])
constraints = []
crossing = [vjrzs, gzcohl]


design=[vjrzs,gzcohl]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_3"))

### END