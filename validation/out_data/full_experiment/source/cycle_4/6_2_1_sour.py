from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
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
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_1_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
