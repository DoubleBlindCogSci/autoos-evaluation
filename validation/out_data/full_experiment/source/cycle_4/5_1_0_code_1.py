from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
emmn = Factor("emmn", ["zfeun", "ulfa"])
qoz = Factor("qoz", ["zoe", "qdaza"])
upqhqx = Factor("upqhqx", ["zfeun", "ulfa"])
gvpmo = Factor("gvpmo", ["zoe", "qdaza"])
hdjam = Factor("hdjam", ["uhe", "oulgv"])
def xjhmo (gvpmo, qoz):
    return gvpmo == qoz
def ieja (gvpmo, qoz):
    return not xjhmo(gvpmo, qoz)
qus = Factor("qus", [DerivedLevel("mwsa", WithinTrial(xjhmo, [gvpmo, qoz])), DerivedLevel("oocxp", WithinTrial(ieja, [gvpmo, qoz]))])
design=[qus,emmn,qoz,upqhqx,gvpmo,hdjam]
constraints=[]
crossing=[qoz,hdjam]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_1_0"))
