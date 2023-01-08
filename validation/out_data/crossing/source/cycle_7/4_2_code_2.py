from sweetpea import *
import os
_dir=os.path.dirname(__file__)
ujghq = Factor("ujghq", ["ptz", "dxkffl"])
pmxb = Factor("pmxb", ["pvyjyc", "zumlf"])
bxst = Factor("bxst", ["tayjxe", "hhxpo"])
tmk = Factor("tmk", ["nus", "czsoi"])
constraints = []
crossing = [ujghq, pmxb, bxst, tmk]


design=[ujghq,pmxb,bxst,tmk]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2"))

### END