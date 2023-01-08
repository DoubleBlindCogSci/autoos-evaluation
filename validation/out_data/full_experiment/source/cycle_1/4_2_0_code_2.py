from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
qzek = Factor("qzek", ["obt", "crkyja"])
wvzc = Factor("wvzc", ["gcwqk", "bpufk"])
pejrm = Factor("pejrm", ["obt", "crkyja"])
gyi = Factor("gyi", ["gcwqk", "bpufk"])
def is_ljk_kxcbx(qzek, wvzc):
    return qzek == wvzc
def is_ljk_qcge(qzek, wvzc):
    return not is_ljk_kxcbx(qzek, wvzc)
ljk= Factor("ljk", [DerivedLevel("kxcbx", WithinTrial(is_ljk_kxcbx, [qzek, wvzc])), DerivedLevel("qcge", WithinTrial(is_ljk_qcge, [qzek, wvzc]))])
def is_htotnl_thnf(gyi, pejrm):
    return gyi == pejrm
def is_htotnl_iacvkn(gyi, pejrm):
    return not is_htotnl_thnf(gyi, pejrm)
htotnl= Factor("htotnl", [DerivedLevel("thnf", WithinTrial(is_htotnl_thnf, [gyi, pejrm])), DerivedLevel("iacvkn", WithinTrial(is_htotnl_iacvkn, [gyi, pejrm]))])
constraints = []
crossing = [ljk, pejrm]

design=[qzek,wvzc,pejrm,gyi, ljk, htotnl]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/4_2_0"))
