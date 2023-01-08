from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
wxkp = Factor("wxkp", ["iqsqug", "ygc"])
fgiigi = Factor("fgiigi", ["ukk", "nojgu"])
vmp = Factor("vmp", ["iqsqug", "ygc"])
fzb = Factor("fzb", ["ukk", "nojgu"])
kpdy = Factor("kpdy", ["hkoia", "mploi"])
def smgg (vmp, fzb):
    return vmp == fzb
def xskmy (vmp, fzb):
    return not smgg(vmp, fzb)
gdzodz = Factor("gdzodz", [DerivedLevel("mwod", WithinTrial(smgg, [vmp, fzb])), DerivedLevel("blf", WithinTrial(xskmy, [vmp, fzb]))])
def fdl (fgiigi, wxkp):
    return fgiigi == wxkp
def hgw (fgiigi, wxkp):
    return not fdl(fgiigi, wxkp)
bbo = Factor("bbo", [DerivedLevel("dxh", WithinTrial(fdl, [fgiigi, wxkp])), DerivedLevel("hox", WithinTrial(hgw, [fgiigi, wxkp]))])
design=[gdzodz,bbo,wxkp,fgiigi,vmp,fzb,kpdy]
constraints=[AtMostKInARow(2, fgiigi),AtLeastKInARow(3, gdzodz)]
crossing=[fzb,gdzodz]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_2_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
