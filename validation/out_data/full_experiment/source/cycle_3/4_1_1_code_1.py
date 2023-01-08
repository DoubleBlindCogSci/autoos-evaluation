from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
rzadpo = Factor("rzadpo", ["elxlc", "zim"])
tcx = Factor("tcx", ["oile", "tmxtso"])
mpsi = Factor("mpsi", ["elxlc", "zim"])
qqsuu = Factor("qqsuu", ["oile", "tmxtso"])
def mfrcwh (qqsuu, rzadpo):
    return qqsuu == rzadpo
def rqhax (qqsuu, rzadpo):
    return not mfrcwh(qqsuu, rzadpo)
zyhs = Factor("zyhs", [DerivedLevel("fxyqp", WithinTrial(mfrcwh, [qqsuu, rzadpo])), DerivedLevel("nljia", WithinTrial(rqhax, [qqsuu, rzadpo]))])
design=[zyhs,rzadpo,tcx,mpsi,qqsuu]
constraints=[AtMostKInARow(4, zyhs)]
crossing=[rzadpo,tcx]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_1_1"))
