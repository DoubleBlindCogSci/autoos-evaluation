from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
mws = Factor("mws", ["rwtfmd", "nqym"])
foz = Factor("foz", ["frp", "mcwtms"])
fnki = Factor("fnki", ["rwtfmd", "nqym"])
mqjb = Factor("mqjb", ["frp", "mcwtms"])
joon = Factor("joon", ["cmuq", "pmuo"])
gfttb = Factor("gfttb", ["vhsq", "zuzdel"])
def wcoulf (gfttb, mqjb):
    return gfttb == mqjb
def dkcb (gfttb, mqjb):
    return not wcoulf(gfttb, mqjb)
bgysdr = Factor("bgysdr", [DerivedLevel("mzqo", WithinTrial(wcoulf, [gfttb, mqjb])), DerivedLevel("cgvco", WithinTrial(dkcb, [gfttb, mqjb]))])
def knbqyn (mws, fnki):
    return mws == fnki
def uuy (mws, fnki):
    return not knbqyn(mws, fnki)
nxivbj = Factor("nxivbj", [DerivedLevel("dgkhjr", WithinTrial(knbqyn, [mws, fnki])), DerivedLevel("kyst", WithinTrial(uuy, [mws, fnki]))])
design=[bgysdr,nxivbj,mws,foz,fnki,mqjb,joon,gfttb]
constraints=[ExactlyKInARow(3, bgysdr)]
crossing=[joon,nxivbj]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_1"))
