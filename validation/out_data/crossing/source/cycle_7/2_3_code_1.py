from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vjrzs = Factor("vjrzs", ["ymzbup", "jrtvj"])
gzcohl = Factor("gzcohl", ["yrrch", "kyrlkh"])

### EXPERIMENT
design=[vjrzs,gzcohl]
crossing=[[vjrzs,gzcohl]]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_3"))
### END