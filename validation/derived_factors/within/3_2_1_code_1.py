from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
rrjaqh = Factor("rrjaqh", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
judsc = Factor("judsc", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
tig = Factor("tig", ["nyyw","fhk","ntd","dwqqqw","pvwnq","ity","ktqi"])
def uehmr(rrjaqh, judsc, tig):
     return rrjaqh == judsc
def raq(rrjaqh, judsc, tig):
     return judsc != rrjaqh and rrjaqh == tig
def dwn(rrjaqh, judsc, tig):
     return (not uehmr(rrjaqh, judsc, tig)) and (not rrjaqh == tig)
dwylr = DerivedLevel("vbejzt", WithinTrial(uehmr, [rrjaqh, judsc, tig]))
sjfs = DerivedLevel("vdj", WithinTrial(raq, [rrjaqh, judsc, tig]))
kso = DerivedLevel("pnph", WithinTrial(dwn, [rrjaqh, judsc, tig]))
njpn = Factor("iaca", [dwylr, sjfs, kso])

### EXPERIMENT
design=[rrjaqh,judsc,tig,njpn]
crossing=[njpn]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_1"))
### END