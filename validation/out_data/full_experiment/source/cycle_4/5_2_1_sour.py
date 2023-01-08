from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
kpdmg = Factor("kpdmg", ["psclbm", "lij"])
olgh = Factor("olgh", ["qru", "lseg"])
ipxtj = Factor("ipxtj", ["psclbm", "lij"])
pdjwng = Factor("pdjwng", ["qru", "lseg"])
yuou = Factor("yuou", ["otpq", "zgqit"])
def ftkodo (olgh, kpdmg):
    return olgh == kpdmg
def vzdhzl (olgh, kpdmg):
    return not ftkodo(olgh, kpdmg)
uibycy = Factor("uibycy", [DerivedLevel("mdp", WithinTrial(ftkodo, [olgh, kpdmg])), DerivedLevel("kjvo", WithinTrial(vzdhzl, [olgh, kpdmg]))])
def vazie (pdjwng, yuou):
    return pdjwng == yuou
def yqyyqi (pdjwng, yuou):
    return not vazie(pdjwng, yuou)
mpxrez = Factor("mpxrez", [DerivedLevel("ncv", WithinTrial(vazie, [pdjwng, yuou])), DerivedLevel("xygm", WithinTrial(yqyyqi, [pdjwng, yuou]))])
design=[uibycy,mpxrez,kpdmg,olgh,ipxtj,pdjwng,yuou]
constraints=[AtLeastKInARow(4, ipxtj)]
crossing=[olgh,uibycy]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_1_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
