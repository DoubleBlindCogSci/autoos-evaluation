from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
jjywqq = Factor("jjywqq", ["ybtpmi", "lqlydm"])
tjwatw = Factor("tjwatw", ["qezqa", "dypoob"])
eayq = Factor("eayq", ["ybtpmi", "lqlydm"])
zlt = Factor("zlt", ["qezqa", "dypoob"])
wgjkb = Factor("wgjkb", ["vajuv", "kapoyj"])
gmrf = Factor("gmrf", ["licx", "qgi"])
def is_gho_dnvcxo(gmrf, zlt):
    return gmrf == zlt
def is_gho_fhuy(gmrf, zlt):
    return not is_gho_dnvcxo(gmrf, zlt)
gho = Factor("gho", [DerivedLevel("dnvcxo", WithinTrial(is_gho_dnvcxo, [gmrf, zlt])), DerivedLevel("fhuy", WithinTrial(is_gho_fhuy, [gmrf, zlt]))])
def is_tvz_wsalj(wgjkb, tjwatw):
    return wgjkb == tjwatw
def is_tvz_lopa(wgjkb, tjwatw):
    return not is_tvz_wsalj(wgjkb, tjwatw)
tvz = Factor("tvz", [DerivedLevel("wsalj", WithinTrial(is_tvz_wsalj, [wgjkb, tjwatw])), DerivedLevel("lopa", WithinTrial(is_tvz_lopa, [wgjkb, tjwatw]))])
constraints = [MinimumTrials(25), ExactlyK(2, (tjwatw, "qezqa"))]
crossing = [eayq, gho]

design=[jjywqq,tjwatw,eayq,zlt,wgjkb,gmrf,gho,tvz]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_2"))
