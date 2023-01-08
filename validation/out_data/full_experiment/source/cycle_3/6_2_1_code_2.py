from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
avbwpg = Factor("avbwpg", ["cimg", "hbfe"])
xzx = Factor("xzx", ["fsk", "nnbtc"])
qrtckt = Factor("qrtckt", ["cimg", "hbfe"])
zomk = Factor("zomk", ["fsk", "nnbtc"])
dergv = Factor("dergv", ["sxzdej", "rxwuo"])
ubzdcu = Factor("ubzdcu", ["vdom", "mqg"])
def is_ftmaw_nch(xzx, ubzdcu):
    return xzx == ubzdcu
def is_ftmaw_mfdpop(xzx, ubzdcu):
    return not is_ftmaw_nch(xzx, ubzdcu)
ftmaw = Factor("ftmaw", [DerivedLevel("nch", WithinTrial(is_ftmaw_nch, [xzx, ubzdcu])), DerivedLevel("mfdpop", WithinTrial(is_ftmaw_mfdpop, [xzx, ubzdcu]))])
def is_upva_gukug(qrtckt, dergv):
    return qrtckt == dergv
def is_upva_bseu(qrtckt, dergv):
    return not is_upva_gukug(qrtckt, dergv)
upva = Factor("upva", [DerivedLevel("gukug", WithinTrial(is_upva_gukug, [qrtckt, dergv])), DerivedLevel("bseu", WithinTrial(is_upva_bseu, [qrtckt, dergv]))])
constraints = [MinimumTrials(29)]
crossing = [dergv, zomk]

design=[avbwpg,xzx,qrtckt,zomk,dergv,ubzdcu,ftmaw,upva]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_1"))
