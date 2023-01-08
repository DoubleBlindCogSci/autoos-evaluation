from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hxj = Factor("hxj", ["tfyil", "lzwr"])
ylxg = Factor("ylxg", ["xjmpuv", "eawolz"])
constraints = []
crossing = [hxj, ylxg]


design=[hxj,ylxg]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_3"))

### END