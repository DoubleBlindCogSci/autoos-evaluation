from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
toll = Factor("toll", ["nqwgeu", "wwudy"])
pkkm = Factor("pkkm", ["khun", "bkyhp"])
hhizte = Factor("hhizte", ["nqwgeu", "wwudy"])
rhl = Factor("rhl", ["khun", "bkyhp"])
def is_cwh_zdljt(rhl, hhizte):
    return rhl == hhizte
def is_cwh_blukz(rhl, hhizte):
    return not is_cwh_zdljt(rhl, hhizte)
cwh = Factor("cwh", [DerivedLevel("zdljt", WithinTrial(is_cwh_zdljt, [rhl, hhizte])), DerivedLevel("blukz", WithinTrial(is_cwh_blukz, [rhl, hhizte]))])
def is_hnt_rjvf(pkkm, toll):
    return pkkm == toll
def is_hnt_qoemb(pkkm, toll):
    return not is_hnt_rjvf(pkkm, toll)
hnt = Factor("hnt", [DerivedLevel("rjvf", WithinTrial(is_hnt_rjvf, [pkkm, toll])), DerivedLevel("qoemb", WithinTrial(is_hnt_qoemb, [pkkm, toll]))])
constraints = [AtLeastKInARow(4, hhizte), MinimumTrials(36)]
crossing = [toll, hhizte]

design=[toll,pkkm,hhizte,rhl,cwh,hnt]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_2"))
