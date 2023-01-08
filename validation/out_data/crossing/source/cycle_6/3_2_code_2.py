from sweetpea import *
import os
_dir=os.path.dirname(__file__)
csuioi = Factor("csuioi", ["vtemh", "ypyzf"])
fbjbz = Factor("fbjbz", ["tjyjs", "aifmvw"])
uweqnl = Factor("uweqnl", ["gbzrj", "dntrjv"])
xoxcg = Factor("xoxcg", ["onu", "fmlioq"])
bemrg = Factor("bemrg", ["ckast", "occul"])
hshkp = Factor("hshkp", ["zxb", "pmjch"])
constraints = []
crossing = [[csuioi, fbjbz], [uweqnl, xoxcg], [bemrg, hshkp]]


design=[csuioi,fbjbz,uweqnl,xoxcg,bemrg,hshkp]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2"))

### END