from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
toll = Factor("toll", ["nqwgeu", "wwudy"])
pkkm = Factor("pkkm", ["khun", "bkyhp"])
hhizte = Factor("hhizte", ["nqwgeu", "wwudy"])
rhl = Factor("rhl", ["khun", "bkyhp"])
def bpae (rhl, hhizte):
    return rhl == hhizte
def ygh (rhl, hhizte):
    return not bpae(rhl, hhizte)
cwh = Factor("cwh", [DerivedLevel("zdljt", WithinTrial(bpae, [rhl, hhizte])), DerivedLevel("blukz", WithinTrial(ygh, [rhl, hhizte]))])
def lfaj (pkkm, toll):
    return pkkm == toll
def sml (pkkm, toll):
    return not lfaj(pkkm, toll)
hnt = Factor("hnt", [DerivedLevel("rjvf", WithinTrial(lfaj, [pkkm, toll])), DerivedLevel("qoemb", WithinTrial(sml, [pkkm, toll]))])
design=[cwh,hnt,toll,pkkm,hhizte,rhl]
constraints=[MinimumTrials(36),AtLeastKInARow(4, hhizte)]
crossing=[toll,hhizte]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_2"))
