from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
rzadpo = Factor("rzadpo", ["elxlc", "zim"])
tcx = Factor("tcx", ["oile", "tmxtso"])
mpsi = Factor("mpsi", ["elxlc", "zim"])
qqsuu = Factor("qqsuu", ["oile", "tmxtso"])
def mfrcwh (qqsuu, rzadpo):
    return qqsuu == rzadpo
def rqhax (qqsuu, rzadpo):
    return not mfrcwh(qqsuu, rzadpo)
zyhs = Factor("zyhs", [DerivedLevel("fxyqp", WithinTrial(mfrcwh, [qqsuu, rzadpo])), DerivedLevel("nljia", WithinTrial(rqhax, [qqsuu, rzadpo]))])
design=[zyhs,rzadpo,tcx,mpsi,qqsuu]
constraints=[AtMostKInARow(4, zyhs)]
crossing=[rzadpo,tcx]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_1_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
