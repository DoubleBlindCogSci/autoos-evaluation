from sweetpea import *
import os
_dir=os.path.dirname(__file__)
twun = Factor("twun", ["nszlmb", "sqkmmp"])
dbrqfp = Factor("dbrqfp", ["vbbf", "ybuw"])
xcoegy = Factor("xcoegy", ["zqhj", "nppxkn"])
wzuzl = Factor("wzuzl", ["jcvii", "bqpv"])
qcz = Factor("qcz", ["nzss", "hba"])
constraints = []
crossing = [twun, dbrqfp, xcoegy, wzuzl, qcz]


design=[twun,dbrqfp,xcoegy,wzuzl,qcz]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2"))

### END