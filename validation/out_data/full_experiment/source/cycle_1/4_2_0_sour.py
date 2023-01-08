from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
qzek = Factor("qzek", ["obt", "crkyja"])
wvzc = Factor("wvzc", ["gcwqk", "bpufk"])
pejrm = Factor("pejrm", ["obt", "crkyja"])
gyi = Factor("gyi", ["gcwqk", "bpufk"])
def nmzq (qzek, wvzc):
    return qzek == wvzc
def sci (qzek, wvzc):
    return not nmzq(qzek, wvzc)
ljk = Factor("ljk", [DerivedLevel("kxcbx", WithinTrial(nmzq, [qzek, wvzc])), DerivedLevel("qcge", WithinTrial(sci, [qzek, wvzc]))])
def yyitno (gyi, pejrm):
    return gyi == pejrm
def leeeii (gyi, pejrm):
    return not yyitno(gyi, pejrm)
htotnl = Factor("htotnl", [DerivedLevel("thnf", WithinTrial(yyitno, [gyi, pejrm])), DerivedLevel("iacvkn", WithinTrial(leeeii, [gyi, pejrm]))])
design=[ljk,htotnl,qzek,wvzc,pejrm,gyi]
constraints=None
crossing=[ljk,pejrm]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_2_0_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
