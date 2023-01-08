from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
rwbf = Factor("rwbf", ["wnxvop", "xpjtji"])
pfval = Factor("pfval", ["vxwj", "nwvr"])
tmqk = Factor("tmqk", ["wnxvop", "xpjtji"])
zay = Factor("zay", ["vxwj", "nwvr"])
axn = Factor("axn", ["ifj", "wrhjrn"])
dwra = Factor("dwra", ["nbowyy", "jxen"])
def gmjvnf (rwbf, tmqk):
    return rwbf == tmqk
def eegjyq (rwbf, tmqk):
    return not gmjvnf(rwbf, tmqk)
wwbdfd = Factor("wwbdfd", [DerivedLevel("stfge", WithinTrial(gmjvnf, [rwbf, tmqk])), DerivedLevel("gfxw", WithinTrial(eegjyq, [rwbf, tmqk]))])
def mwbtm (pfval, dwra):
    return pfval == dwra
def tgdade (pfval, dwra):
    return not mwbtm(pfval, dwra)
zyaxqg = Factor("zyaxqg", [DerivedLevel("oxlyic", WithinTrial(mwbtm, [pfval, dwra])), DerivedLevel("cmfig", WithinTrial(tgdade, [pfval, dwra]))])
design=[wwbdfd,zyaxqg,rwbf,pfval,tmqk,zay,axn,dwra]
constraints=[AtMostKInARow(2, wwbdfd)]
crossing=[dwra,zyaxqg]
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
