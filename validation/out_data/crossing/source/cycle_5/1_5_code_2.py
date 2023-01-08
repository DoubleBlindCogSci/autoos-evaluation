from sweetpea import *
import os
_dir=os.path.dirname(__file__)
mmm = Factor("mmm", ["mzzxwp", "miykj"])
kdxsv = Factor("kdxsv", ["wgjucg", "bshvjr"])
constraints = []
crossing = [mmm, kdxsv]


design=[mmm,kdxsv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/1_5"))

### END