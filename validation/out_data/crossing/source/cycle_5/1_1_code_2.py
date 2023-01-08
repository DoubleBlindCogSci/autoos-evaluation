from sweetpea import *
import os
_dir=os.path.dirname(__file__)
mbnlqm = Factor("mbnlqm", ["nou", "dpaqdj"])
oyc = Factor("oyc", ["ojfy", "nluriz"])
constraints = []
crossing = [mbnlqm, oyc]


design=[mbnlqm,oyc]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_1"))

### END