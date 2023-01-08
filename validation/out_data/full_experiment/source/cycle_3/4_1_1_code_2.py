from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
rzadpo = Factor("rzadpo", ["elxlc", "zim"])
tcx = Factor("tcx", ["oile", "tmxtso"])
mpsi = Factor("mpsi", ["elxlc", "zim"])
qqsuu = Factor("qqsuu", ["oile", "tmxtso"])
def is_zyhs_fxyqp(qqsuu, rzadpo):
    return qqsuu == rzadpo
def is_zyhs_nljia(qqsuu, rzadpo):
    return not is_zyhs_fxyqp(qqsuu, rzadpo)
zyhs = Factor("zyhs", [DerivedLevel("fxyqp", WithinTrial(is_zyhs_fxyqp, [qqsuu, rzadpo])), DerivedLevel("nljia", WithinTrial(is_zyhs_nljia, [qqsuu, rzadpo]))])
constraints = [AtMostKInARow(4, zyhs)]
crossing = [rzadpo, tcx]

design=[rzadpo,tcx,mpsi,qqsuu,zyhs]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_1_1"))
