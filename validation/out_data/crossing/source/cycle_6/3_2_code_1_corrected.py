from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
csuioi = Factor("csuioi", ["vtemh", "ypyzf"])
fbjbz = Factor("fbjbz", ["tjyjs", "aifmvw"])
uweqnl = Factor("uweqnl", ["gbzrj", "dntrjv"])
xoxcg = Factor("xoxcg", ["onu", "fmlioq"])
bemrg = Factor("bemrg", ["ckast", "occul"])
hshkp = Factor("hshkp", ["zxb", "pmjch"])

### EXPERIMENT
design=[csuioi,fbjbz,uweqnl,xoxcg,bemrg,hshkp]
crossing = [[uweqnl,xoxcg],[bemrg,hshkp],[csuioi,fbjbz],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1,IterateGen)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2"))
### END
