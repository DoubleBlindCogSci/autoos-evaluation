from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
mws = Factor("mws", ["rwtfmd", "nqym"])
foz = Factor("foz", ["frp", "mcwtms"])
fnki = Factor("fnki", ["rwtfmd", "nqym"])
mqjb = Factor("mqjb", ["frp", "mcwtms"])
joon = Factor("joon", ["cmuq", "pmuo"])
gfttb = Factor("gfttb", ["vhsq", "zuzdel"])
def is_bgysdr_mzqo(gfttb, mqjb):
    return gfttb == mqjb
def is_bgysdr_cgvco(gfttb, mqjb):
    return not is_bgysdr_mzqo(gfttb, mqjb)
bgysdr = Factor("bgysdr", [DerivedLevel("mzqo", WithinTrial(is_bgysdr_mzqo, [gfttb, mqjb])), DerivedLevel("cgvco", WithinTrial(is_bgysdr_cgvco, [gfttb, mqjb]))])
def is_nxivbj_dgkhjr(mws, fnki):
    return mws == fnki
def is_nxivbj_kyst(mws, fnki):
    return not is_nxivbj_dgkhjr(mws, fnki)
nxivbj = Factor("nxivbj", [DerivedLevel("dgkhjr", WithinTrial(is_nxivbj_dgkhjr, [mws, fnki])), DerivedLevel("kyst", WithinTrial(is_nxivbj_kyst, [mws, fnki]))])
constraints = [ExactlyKInARow(3, (bgysdr, "mzqo"))]
crossing = [joon, nxivbj]

design=[mws,foz,fnki,mqjb,joon,gfttb,bgysdr,nxivbj]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_1"))
