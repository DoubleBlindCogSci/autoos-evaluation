from sweetpea import *
import os
_dir=os.path.dirname(__file__)
yyaxty = Factor("yyaxty", ["vlni", "gic"])
tovgxc = Factor("tovgxc", ["uvqg", "wasrf"])
unbw = Factor("unbw", ["bnb", "llma"])
mdfbrh = Factor("mdfbrh", ["icennq", "kkkyp"])
nboknq = Factor("nboknq", ["kmvca", "dcg"])
usiemr = Factor("usiemr", ["pnztwr", "dgxxhf"])
constraints = []
crossing = [[yyaxty], [tovgxc], [unbw, mdfbrh, nboknq], [usiemr]]


design=[yyaxty,tovgxc,unbw,mdfbrh,nboknq,usiemr]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_0"))

### END