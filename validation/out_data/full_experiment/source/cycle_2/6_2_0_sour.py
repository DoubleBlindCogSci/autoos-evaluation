from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
engo = Factor("engo", ["lbjuv", "dyo"])
kctkp = Factor("kctkp", ["izl", "rgaqux"])
vnp = Factor("vnp", ["lbjuv", "dyo"])
qid = Factor("qid", ["izl", "rgaqux"])
itpxp = Factor("itpxp", ["jpnqdt", "uai"])
gxh = Factor("gxh", ["gbrd", "ncogvs"])
def axzd (vnp, gxh):
    return vnp == gxh
def kzi (vnp, gxh):
    return not axzd(vnp, gxh)
jfvhy = Factor("jfvhy", [DerivedLevel("gqppy", WithinTrial(axzd, [vnp, gxh])), DerivedLevel("nyza", WithinTrial(kzi, [vnp, gxh]))])
def mcun (engo, qid):
    return engo == qid
def gtj (engo, qid):
    return not mcun(engo, qid)
oclt = Factor("oclt", [DerivedLevel("vbw", WithinTrial(mcun, [engo, qid])), DerivedLevel("qqz", WithinTrial(gtj, [engo, qid]))])
design=[jfvhy,oclt,engo,kctkp,vnp,qid,itpxp,gxh]
constraints=[]
crossing=[jfvhy,itpxp]
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
