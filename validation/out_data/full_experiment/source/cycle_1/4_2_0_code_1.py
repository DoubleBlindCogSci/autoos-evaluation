from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
qzek = Factor("qzek", ["obt", "crkyja"])
wvzc = Factor("wvzc", ["gcwqk", "bpufk"])
pejrm = Factor("pejrm", ["obt", "crkyja"])
gyi = Factor("gyi", ["gcwqk", "bpufk"])
def nmzq (qzek, wvzc):
    return qzek == wvzc
def sci (qzek, wvzc):
    return not nmzq(qzek, wvzc)
ljk = Factor("ljk", [DerivedLevel("kxcbx", WithinTrial(nmzq, [qzek, wvzc])), DerivedLevel("qcge", WithinTrial(sci, [qzek, wvzc]))])
def yyitno (gyi, pejrm):
    return gyi == pejrm
def leeeii (gyi, pejrm):
    return not yyitno(gyi, pejrm)
htotnl = Factor("htotnl", [DerivedLevel("thnf", WithinTrial(yyitno, [gyi, pejrm])), DerivedLevel("iacvkn", WithinTrial(leeeii, [gyi, pejrm]))])
design=[ljk,htotnl,qzek,wvzc,pejrm,gyi]
constraints=[]
crossing=[ljk,pejrm]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/4_2_0"))
