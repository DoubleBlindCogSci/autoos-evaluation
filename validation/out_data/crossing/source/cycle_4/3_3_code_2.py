from sweetpea import *
import os
_dir=os.path.dirname(__file__)
hqprq = Factor("hqprq", ["uiukoq", "mwwmjt"])
nojzr = Factor("nojzr", ["tqjxm", "aktrgm"])
izxwg = Factor("izxwg", ["bxbrh", "ipq"])
tola = Factor("tola", ["drlmk", "pucl"])
xrfvnt = Factor("xrfvnt", ["zto", "bipe"])
xfqckj = Factor("xfqckj", ["ptrv", "wedek"])
doyf = Factor("doyf", ["xolhdn", "wilzr"])
constraints = []
crossing = [[hqprq, nojzr], [izxwg, tola, xrfvnt, xfqckj], [doyf]]


design=[hqprq,nojzr,izxwg,tola,xrfvnt,xfqckj,doyf]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_3"))

### END