from sweetpea import *
import os
_dir=os.path.dirname(__file__)
kfn = Factor("kfn", ["yxl", "bcomrr"])
fxnb = Factor("fxnb", ["jyqgj", "vcj"])
nfneo = Factor("nfneo", ["wrk", "mes"])
yeorq = Factor("yeorq", ["gdrghk", "zddjuj"])
alfwgo = Factor("alfwgo", ["zeb", "wqiwq"])
constraints = []
crossing = [[kfn], [fxnb, nfneo, yeorq, alfwgo]]


design=[kfn,fxnb,nfneo,yeorq,alfwgo]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1"))

### END