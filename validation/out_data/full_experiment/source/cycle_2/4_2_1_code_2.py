from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
oxt = Factor("oxt", ["sivho", "cqbgic"])
jvg = Factor("jvg", ["ohs", "wpyrc"])
moskvk = Factor("moskvk", ["sivho", "cqbgic"])
ijmr = Factor("ijmr", ["ohs", "wpyrc"])
def is_knmejn_dhmqoa(ijmr, moskvk):
    return ijmr == moskvk
def is_knmejn_tgtul(ijmr, moskvk):
    return not is_knmejn_dhmqoa(ijmr, moskvk)
knmejn= Factor("knmejn", [DerivedLevel("dhmqoa", WithinTrial(is_knmejn_dhmqoa, [ijmr, moskvk])), DerivedLevel("tgtul", WithinTrial(is_knmejn_tgtul, [ijmr, moskvk]))])
def is_imxuu_ajirpt(oxt, jvg):
    return oxt == jvg
def is_imxuu_nozlj(oxt, jvg):
    return not is_imxuu_ajirpt(oxt, jvg)
imxuu= Factor("imxuu", [DerivedLevel("ajirpt", WithinTrial(is_imxuu_ajirpt, [oxt, jvg])), DerivedLevel("nozlj", WithinTrial(is_imxuu_nozlj, [oxt, jvg]))])
constraints = [AtMostKInARow(2, oxt)]
crossing = [moskvk, oxt]

design=[oxt,jvg,moskvk,ijmr,knmejn,imxuu]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_2_1"))
