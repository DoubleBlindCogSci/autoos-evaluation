from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
rdofu = Factor("rdofu", ["pyobz", "ofkrum"])
knakml = Factor("knakml", ["qubuk", "dok"])
qnpxs = Factor("qnpxs", ["pyobz", "ofkrum"])
vwpw = Factor("vwpw", ["qubuk", "dok"])
dyti = Factor("dyti", ["hpcxbk", "nfp"])
def is_qad_iast(knakml, dyti):
    return knakml == dyti
def is_qad_mlsvfv(knakml, dyti):
    return not is_qad_iast(knakml, dyti)
qad= Factor("qad", [DerivedLevel("iast", WithinTrial(is_qad_iast, [knakml, dyti])), DerivedLevel("mlsvfv", WithinTrial(is_qad_mlsvfv, [knakml, dyti]))])
def is_kho_eedltm(vwpw, rdofu):
    return vwpw == rdofu
def is_kho_ived(vwpw, rdofu):
    return not is_kho_eedltm(vwpw, rdofu)
kho= Factor("kho", [DerivedLevel("eedltm", WithinTrial(is_kho_eedltm, [vwpw, rdofu])), DerivedLevel("ived", WithinTrial(is_kho_ived, [vwpw, rdofu]))])
constraints = []
crossing = [kho, vwpw]

design=[rdofu,knakml,qnpxs,vwpw,dyti,qad,kho]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/5_2_0"))
