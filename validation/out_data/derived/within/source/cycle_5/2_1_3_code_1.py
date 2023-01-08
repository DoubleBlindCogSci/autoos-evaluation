from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zgreiu = Factor("zgreiu", ["tnhg","ychk","lcb","nuk","gmao"])
def ysrw(zgreiu):
    return zgreiu == "ychk"
def mkt(zgreiu):
    return not ysrw(zgreiu)
hheeo = Factor("eagfi", [DerivedLevel("elbbb", WithinTrial(ysrw, [zgreiu])), DerivedLevel("pcpop", WithinTrial(mkt, [zgreiu]))])
### EXPERIMENT
design=[zgreiu,hheeo]
crossing=[hheeo]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_1_3"))
### END