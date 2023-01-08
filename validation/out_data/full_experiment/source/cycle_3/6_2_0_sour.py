from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
uirvdf = Factor("uirvdf", ["ljjzo", "vmds"])
skcfby = Factor("skcfby", ["bwls", "jbj"])
imowog = Factor("imowog", ["ljjzo", "vmds"])
lwou = Factor("lwou", ["bwls", "jbj"])
sws = Factor("sws", ["pewpg", "jniby"])
wfhvd = Factor("wfhvd", ["pmjf", "xrzjqz"])
def ymjp (imowog, wfhvd):
    return imowog == wfhvd
def xodrv (imowog, wfhvd):
    return not ymjp(imowog, wfhvd)
fdp = Factor("fdp", [DerivedLevel("rufmz", WithinTrial(ymjp, [imowog, wfhvd])), DerivedLevel("ssrvcv", WithinTrial(xodrv, [imowog, wfhvd]))])
def egvhq (skcfby, uirvdf):
    return skcfby == uirvdf
def mns (skcfby, uirvdf):
    return not egvhq(skcfby, uirvdf)
xwpnof = Factor("xwpnof", [DerivedLevel("wqvxe", WithinTrial(egvhq, [skcfby, uirvdf])), DerivedLevel("zbc", WithinTrial(mns, [skcfby, uirvdf]))])
design=[fdp,xwpnof,uirvdf,skcfby,imowog,lwou,sws,wfhvd]
constraints=[]
crossing=[wfhvd,sws]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_0_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
