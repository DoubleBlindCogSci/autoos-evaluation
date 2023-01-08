from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
byds = Factor("byds", ["wnsa", "pbvws"])
zqhjpa = Factor("zqhjpa", ["auo", "ikosc"])
ppktzu = Factor("ppktzu", ["wnsa", "pbvws"])
bwci = Factor("bwci", ["auo", "ikosc"])
rxukub = Factor("rxukub", ["txxm", "yojoxb"])
def is_cznezw_fzjgi(bwci, rxukub):
    return bwci == rxukub
def is_cznezw_qpqg(bwci, rxukub):
    return not is_cznezw_fzjgi(bwci, rxukub)
cznezw = Factor("cznezw", [DerivedLevel("fzjgi", WithinTrial(is_cznezw_fzjgi, [bwci, rxukub])), DerivedLevel("qpqg", WithinTrial(is_cznezw_qpqg, [bwci, rxukub]))])
def is_gabz_grwuc(byds, zqhjpa):
    return byds == zqhjpa
def is_gabz_tysmu(byds, zqhjpa):
    return not is_gabz_grwuc(byds, zqhjpa)
gabz = Factor("gabz", [DerivedLevel("grwuc", WithinTrial(is_gabz_grwuc, [byds, zqhjpa])), DerivedLevel("tysmu", WithinTrial(is_gabz_tysmu, [byds, zqhjpa]))])
constraints = []
crossing = [byds, ppktzu]

design=[byds,zqhjpa,ppktzu,bwci,rxukub,cznezw,gabz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_0"))
