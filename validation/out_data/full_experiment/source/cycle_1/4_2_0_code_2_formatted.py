### REGULAR FACTORS
qzek = Factor("qzek", ["obt", "crkyja"])
wvzc = Factor("wvzc", ["gcwqk", "bpufk"])
pejrm = Factor("pejrm", ["obt", "crkyja"])
gyi = Factor("gyi", ["gcwqk", "bpufk"])
### DERIVED FACTORS
##
def is_ljk_kxcbx(qzek, wvzc):
    return qzek == wvzc
def is_ljk_qcge(qzek, wvzc):
    return not is_ljk_kxcbx(qzek, wvzc)
ljk= Factor("ljk", [DerivedLevel("kxcbx", WithinTrial(is_ljk_kxcbx, [qzek, wvzc])), DerivedLevel("qcge", WithinTrial(is_ljk_qcge, [qzek, wvzc]))])
##
def is_htotnl_thnf(gyi, pejrm):
    return gyi == pejrm
def is_htotnl_iacvkn(gyi, pejrm):
    return not is_htotnl_thnf(gyi, pejrm)
htotnl= Factor("htotnl", [DerivedLevel("thnf", WithinTrial(is_htotnl_thnf, [gyi, pejrm])), DerivedLevel("iacvkn", WithinTrial(is_htotnl_iacvkn, [gyi, pejrm]))])
### EXPERIMENT
constraints = []
crossing = [ljk, pejrm]
design=[qzek,wvzc,pejrm,gyi, ljk, htotnl]
block=CrossBlock(design,crossing,constraints)
### END OF EXPERIMENT DESIGN
