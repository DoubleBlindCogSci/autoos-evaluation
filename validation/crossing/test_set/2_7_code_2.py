from sweetpea import *
import os
_dir=os.path.dirname(__file__)
jlgxj = Factor("jlgxj", ["nvxo", "xbbjkv"])
ewd = Factor("ewd", ["hyb", "pkmd"])
constraints = []
crossing = [jlgxj, ewd]


design=[jlgxj,ewd]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_7"))

### END