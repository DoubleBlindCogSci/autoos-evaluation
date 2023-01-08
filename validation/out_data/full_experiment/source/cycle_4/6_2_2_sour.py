from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
zzikcb = Factor("zzikcb", ["vqfk", "agw"])
vwx = Factor("vwx", ["mgm", "ujhniq"])
wowvt = Factor("wowvt", ["vqfk", "agw"])
vwq = Factor("vwq", ["mgm", "ujhniq"])
fchnpa = Factor("fchnpa", ["cbk", "gvdxnm"])
eiznef = Factor("eiznef", ["trjw", "oerf"])
def sibk (wowvt, zzikcb):
    return wowvt == zzikcb
def bvlpxh (wowvt, zzikcb):
    return not sibk(wowvt, zzikcb)
smr = Factor("smr", [DerivedLevel("izh", WithinTrial(sibk, [wowvt, zzikcb])), DerivedLevel("clwvo", WithinTrial(bvlpxh, [wowvt, zzikcb]))])
def nop (vwx, eiznef):
    return vwx == eiznef
def ivd (vwx, eiznef):
    return not nop(vwx, eiznef)
ulkwbd = Factor("ulkwbd", [DerivedLevel("cvnh", WithinTrial(nop, [vwx, eiznef])), DerivedLevel("ysbpo", WithinTrial(ivd, [vwx, eiznef]))])
design=[smr,ulkwbd,zzikcb,vwx,wowvt,vwq,fchnpa,eiznef]
constraints=[AtLeastKInARow(2, vwx),AtMostKInARow(2, eiznef)]
crossing=[vwx,zzikcb]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_2_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
