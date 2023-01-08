from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rkhed = Factor("rkhed", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
wogtke = Factor("wogtke", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
xato = Factor("xato", ["uarmno","isfq","bdzii","dqz","oqw","seanww","uywzva"])
def yqjp(rkhed, wogtke, xato):
    return rkhed != wogtke and rkhed == xato
def bdhud(rkhed, wogtke, xato):
    return not yqjp(rkhed, wogtke, xato)
rzeqy = DerivedLevel("wxmis", WithinTrial(yqjp, [rkhed, wogtke, xato]))
ppw = DerivedLevel("mjengt", WithinTrial(bdhud, [rkhed, wogtke, xato]))
tzuxy = Factor("uncy", [rzeqy, ppw])

### EXPERIMENT
design=[rkhed,wogtke,xato,tzuxy]
crossing=[tzuxy]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_2"))
### END