from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
jjywqq = Factor("jjywqq", ["ybtpmi", "lqlydm"])
tjwatw = Factor("tjwatw", ["qezqa", "dypoob"])
eayq = Factor("eayq", ["ybtpmi", "lqlydm"])
zlt = Factor("zlt", ["qezqa", "dypoob"])
wgjkb = Factor("wgjkb", ["vajuv", "kapoyj"])
gmrf = Factor("gmrf", ["licx", "qgi"])
def aayt (gmrf, zlt):
    return gmrf == zlt
def sgwj (gmrf, zlt):
    return not aayt(gmrf, zlt)
gho = Factor("gho", [DerivedLevel("dnvcxo", WithinTrial(aayt, [gmrf, zlt])), DerivedLevel("fhuy", WithinTrial(sgwj, [gmrf, zlt]))])
def ntpmux (wgjkb, tjwatw):
    return wgjkb == tjwatw
def lnlfmi (wgjkb, tjwatw):
    return not ntpmux(wgjkb, tjwatw)
tvz = Factor("tvz", [DerivedLevel("wsalj", WithinTrial(ntpmux, [wgjkb, tjwatw])), DerivedLevel("lopa", WithinTrial(lnlfmi, [wgjkb, tjwatw]))])
design=[gho,tvz,jjywqq,tjwatw,eayq,zlt,wgjkb,gmrf]
constraints=[ExactlyKInARow(2, tjwatw),MinimumTrials(25)]
crossing=[eayq,gho]
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
