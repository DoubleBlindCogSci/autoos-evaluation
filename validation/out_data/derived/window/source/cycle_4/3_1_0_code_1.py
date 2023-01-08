from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zdbxi = Factor("zdbxi", ["hcj","pnqr","edln","jtizo","kueg","vid","wzchdg"])
def plwzsb(zdbxi):
     return "pnqr" == zdbxi[-1] and not zdbxi[0] == "pnqr"
def pad(zdbxi):
     return zdbxi[-1] != "pnqr" and  zdbxi[0] == "edln"
def pjbx(zdbxi):
     return (not zdbxi[-1] == "pnqr") and (not pad(zdbxi))
inf = Factor("mfnjeh", [DerivedLevel("nud", Window(plwzsb, [zdbxi],2,1)), DerivedLevel("uah", Window(pad, [zdbxi],2,1)),DerivedLevel("ugi", Window(pjbx, [zdbxi],2,1))])
### EXPERIMENT
design=[zdbxi,inf]
crossing=[inf]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_1_0"))
### END