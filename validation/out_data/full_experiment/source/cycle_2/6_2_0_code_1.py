from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
engo = Factor("engo", ["lbjuv", "dyo"])
kctkp = Factor("kctkp", ["izl", "rgaqux"])
vnp = Factor("vnp", ["lbjuv", "dyo"])
qid = Factor("qid", ["izl", "rgaqux"])
itpxp = Factor("itpxp", ["jpnqdt", "uai"])
gxh = Factor("gxh", ["gbrd", "ncogvs"])
def axzd (vnp, gxh):
    return vnp == gxh
def kzi (vnp, gxh):
    return not axzd(vnp, gxh)
jfvhy = Factor("jfvhy", [DerivedLevel("gqppy", WithinTrial(axzd, [vnp, gxh])), DerivedLevel("nyza", WithinTrial(kzi, [vnp, gxh]))])
def mcun (engo, qid):
    return engo == qid
def gtj (engo, qid):
    return not mcun(engo, qid)
oclt = Factor("oclt", [DerivedLevel("vbw", WithinTrial(mcun, [engo, qid])), DerivedLevel("qqz", WithinTrial(gtj, [engo, qid]))])
design=[jfvhy,oclt,engo,kctkp,vnp,qid,itpxp,gxh]
constraints=[]
crossing=[jfvhy,itpxp]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_0"))
