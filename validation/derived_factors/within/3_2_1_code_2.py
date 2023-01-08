from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
rrjaqh = Factor("rrjaqh", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
judsc = Factor("judsc", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
tig = Factor("tig", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
def is_iaca_vbejzt(rrjaqh, judsc, tig):
    return rrjaqh == judsc
def is_iaca_vdj(rrjaqh, judsc, tig):
    return rrjaqh != judsc and rrjaqh == tig
def is_iaca_pnph(rrjaqh, judsc, tig):
    return not (is_iaca_vbejzt(rrjaqh, judsc, tig) or is_iaca_vdj(rrjaqh, judsc, tig))
iaca = Factor("iaca", [DerivedLevel("vbejzt", WithinTrial(is_iaca_vbejzt, [rrjaqh, judsc, tig])), DerivedLevel("vdj", WithinTrial(is_iaca_vdj, [rrjaqh, judsc, tig])), DerivedLevel("pnph", WithinTrial(is_iaca_pnph, [rrjaqh, judsc, tig]))])

design=[rrjaqh,judsc,tig,iaca]
crossing=[iaca]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_1"))

### END