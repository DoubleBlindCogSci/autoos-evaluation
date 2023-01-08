from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
emmn = Factor("emmn", ["zfeun", "ulfa"])
qoz = Factor("qoz", ["zoe", "qdaza"])
upqhqx = Factor("upqhqx", ["zfeun", "ulfa"])
gvpmo = Factor("gvpmo", ["zoe", "qdaza"])
hdjam = Factor("hdjam", ["uhe", "oulgv"])
def is_qus_mwsa(gvpmo, qoz):
    return gvpmo == qoz
def is_qus_oocxp(gvpmo, qoz):
    return not is_qus_mwsa(gvpmo, qoz)
qus = Factor("qus", [DerivedLevel("mwsa", WithinTrial(is_qus_mwsa, [gvpmo, qoz])), DerivedLevel("oocxp", WithinTrial(is_qus_oocxp, [gvpmo, qoz]))])
constraints = []
crossing = [qoz, hdjam]

design=[emmn,qoz,upqhqx,gvpmo,hdjam,qus]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_1_0"))
