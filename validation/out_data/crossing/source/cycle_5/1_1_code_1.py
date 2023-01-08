from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
mbnlqm = Factor("mbnlqm", ["nou", "dpaqdj"])
oyc = Factor("oyc", ["ojfy", "nluriz"])

### EXPERIMENT
design=[mbnlqm,oyc]
crossing=[[mbnlqm,oyc],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/1_1"))
### END