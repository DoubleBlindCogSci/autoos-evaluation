from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yyaxty = Factor("yyaxty", ["vlni", "gic"])
tovgxc = Factor("tovgxc", ["uvqg", "wasrf"])
unbw = Factor("unbw", ["bnb", "llma"])
mdfbrh = Factor("mdfbrh", ["icennq", "kkkyp"])
nboknq = Factor("nboknq", ["kmvca", "dcg"])
usiemr = Factor("usiemr", ["pnztwr", "dgxxhf"])

### EXPERIMENT
design=[yyaxty,tovgxc,unbw,mdfbrh,nboknq,usiemr]
crossing=[[yyaxty],[tovgxc],[unbw,mdfbrh,nboknq],[usiemr],]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_0"))
### END