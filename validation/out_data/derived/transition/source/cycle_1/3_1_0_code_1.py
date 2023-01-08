from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iraw = Factor("iraw", ["uyv","aiyucw","ofd","yrk","nhzpt","incd"])
def zfexg(iraw):
     return iraw[0] == "ofd"
def xenak(iraw):
     return iraw[-1] == "uyv"
def rumvh(iraw):
     return (not iraw[0] == "ofd") and (not xenak(iraw))
pvtv = Factor("goetv", [DerivedLevel("luve", Transition(zfexg, [iraw])), DerivedLevel("wxp", Transition(xenak, [iraw])),DerivedLevel("zjqnkh", Transition(rumvh, [iraw]))])
### EXPERIMENT
design=[iraw,pvtv]
crossing=[pvtv]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END