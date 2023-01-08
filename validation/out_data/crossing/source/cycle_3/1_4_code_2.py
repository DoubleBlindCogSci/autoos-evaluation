from sweetpea import *
import os
_dir=os.path.dirname(__file__)
xrmdtq = Factor("xrmdtq", ["qsdwuv", "rtel"])
lejj = Factor("lejj", ["czoo", "dnmdzs"])
hqht = Factor("hqht", ["elxnc", "mxzpkv"])
constraints = []
crossing = [xrmdtq, lejj, hqht]


design=[xrmdtq,lejj,hqht]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_4"))

### END