from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rkhed = Factor("rkhed", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
wogtke = Factor("wogtke", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
xato = Factor("xato", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
def is_uncy_wxmis(rkhed, wogtke, xato):
    return rkhed != wogtke and rkhed == xato
def is_uncy_mjengt(rkhed, wogtke, xato):
    return not is_uncy_wxmis(rkhed, wogtke, xato)
uncy = Factor("uncy", [DerivedLevel("wxmis", WithinTrial(is_uncy_wxmis, [rkhed, wogtke, xato])), DerivedLevel("mjengt", WithinTrial(is_uncy_mjengt, [rkhed, wogtke, xato]))])

design=[rkhed,wogtke,xato,uncy]
crossing=[uncy]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_2"))

### END