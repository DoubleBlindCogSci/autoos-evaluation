from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
jjywqq = Factor("jjywqq", ["ybtpmi", "lqlydm"])
tjwatw = Factor("tjwatw", ["qezqa", "dypoob"])
eayq = Factor("eayq", ["ybtpmi", "lqlydm"])
zlt = Factor("zlt", ["qezqa", "dypoob"])
wgjkb = Factor("wgjkb", ["vajuv", "kapoyj"])
gmrf = Factor("gmrf", ["licx", "qgi"])
def aayt (gmrf, zlt):
    return gmrf == zlt
def sgwj (gmrf, zlt):
    return not aayt(gmrf, zlt)
gho = Factor("gho", [DerivedLevel("dnvcxo", WithinTrial(aayt, [gmrf, zlt])), DerivedLevel("fhuy", WithinTrial(sgwj, [gmrf, zlt]))])
def ntpmux (wgjkb, tjwatw):
    return wgjkb == tjwatw
def lnlfmi (wgjkb, tjwatw):
    return not ntpmux(wgjkb, tjwatw)
tvz = Factor("tvz", [DerivedLevel("wsalj", WithinTrial(ntpmux, [wgjkb, tjwatw])), DerivedLevel("lopa", WithinTrial(lnlfmi, [wgjkb, tjwatw]))])
design=[gho,tvz,jjywqq,tjwatw,eayq,zlt,wgjkb,gmrf]
constraints=[ExactlyKInARow(2, tjwatw),MinimumTrials(25)]
crossing=[eayq,gho]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_2"))
