from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
rdofu = Factor("rdofu", ["pyobz", "ofkrum"])
knakml = Factor("knakml", ["qubuk", "dok"])
qnpxs = Factor("qnpxs", ["pyobz", "ofkrum"])
vwpw = Factor("vwpw", ["qubuk", "dok"])
dyti = Factor("dyti", ["hpcxbk", "nfp"])
def lfncx (knakml, dyti):
    return knakml == dyti
def eucmp (knakml, dyti):
    return not lfncx(knakml, dyti)
qad = Factor("qad", [DerivedLevel("iast", WithinTrial(lfncx, [knakml, dyti])), DerivedLevel("mlsvfv", WithinTrial(eucmp, [knakml, dyti]))])
def obcrob (vwpw, rdofu):
    return vwpw == rdofu
def woq (vwpw, rdofu):
    return not obcrob(vwpw, rdofu)
kho = Factor("kho", [DerivedLevel("eedltm", WithinTrial(obcrob, [vwpw, rdofu])), DerivedLevel("ived", WithinTrial(woq, [vwpw, rdofu]))])
design=[qad,kho,rdofu,knakml,qnpxs,vwpw,dyti]
constraints=[]
crossing=[kho,vwpw]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/5_2_0"))
