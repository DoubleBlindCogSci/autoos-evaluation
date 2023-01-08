from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
avbwpg = Factor("avbwpg", ["cimg", "hbfe"])
xzx = Factor("xzx", ["fsk", "nnbtc"])
qrtckt = Factor("qrtckt", ["cimg", "hbfe"])
zomk = Factor("zomk", ["fsk", "nnbtc"])
dergv = Factor("dergv", ["sxzdej", "rxwuo"])
ubzdcu = Factor("ubzdcu", ["vdom", "mqg"])
def jhy (xzx, ubzdcu):
    return xzx == ubzdcu
def zjigs (xzx, ubzdcu):
    return not jhy(xzx, ubzdcu)
ftmaw = Factor("ftmaw", [DerivedLevel("nch", WithinTrial(jhy, [xzx, ubzdcu])), DerivedLevel("mfdpop", WithinTrial(zjigs, [xzx, ubzdcu]))])
def lomu (qrtckt, dergv):
    return qrtckt == dergv
def rycyc (qrtckt, dergv):
    return not lomu(qrtckt, dergv)
upva = Factor("upva", [DerivedLevel("gukug", WithinTrial(lomu, [qrtckt, dergv])), DerivedLevel("bseu", WithinTrial(rycyc, [qrtckt, dergv]))])
design=[ftmaw,upva,avbwpg,xzx,qrtckt,zomk,dergv,ubzdcu]
constraints=[MinimumTrials(29)]
crossing=[dergv,zomk]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_1"))
