from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
oxt = Factor("oxt", ["sivho", "cqbgic"])
jvg = Factor("jvg", ["ohs", "wpyrc"])
moskvk = Factor("moskvk", ["sivho", "cqbgic"])
ijmr = Factor("ijmr", ["ohs", "wpyrc"])
def mlbfmb (ijmr, moskvk):
    return ijmr == moskvk
def zuegl (ijmr, moskvk):
    return not mlbfmb(ijmr, moskvk)
knmejn = Factor("knmejn", [DerivedLevel("dhmqoa", WithinTrial(mlbfmb, [ijmr, moskvk])), DerivedLevel("tgtul", WithinTrial(zuegl, [ijmr, moskvk]))])
def njsh (oxt, jvg):
    return oxt == jvg
def apbpic (oxt, jvg):
    return not njsh(oxt, jvg)
imxuu = Factor("imxuu", [DerivedLevel("ajirpt", WithinTrial(njsh, [oxt, jvg])), DerivedLevel("nozlj", WithinTrial(apbpic, [oxt, jvg]))])
design=[knmejn,imxuu,oxt,jvg,moskvk,ijmr]
constraints=[AtMostKInARow(2, oxt)]
crossing=[moskvk,oxt]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_2_1"))
