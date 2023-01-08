from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
wwr = Factor("wwr", ["tbuiey", "yytduo"])
dnj = Factor("dnj", ["qarhs", "dxt"])
oskly = Factor("oskly", ["tbuiey", "yytduo"])
kny = Factor("kny", ["qarhs", "dxt"])
wgpxd = Factor("wgpxd", ["irlh", "cawso"])
bamy = Factor("bamy", ["qdmmba", "ueqq"])
def hycy (kny, bamy):
    return kny == bamy
def uwp (kny, bamy):
    return not hycy(kny, bamy)
rqrk = Factor("rqrk", [DerivedLevel("gqu", WithinTrial(hycy, [kny, bamy])), DerivedLevel("rrpfp", WithinTrial(uwp, [kny, bamy]))])
def oluf (wwr, oskly):
    return wwr == oskly
def yjofe (wwr, oskly):
    return not oluf(wwr, oskly)
sppmi = Factor("sppmi", [DerivedLevel("wzd", WithinTrial(oluf, [wwr, oskly])), DerivedLevel("pnrapu", WithinTrial(yjofe, [wwr, oskly]))])
design=[rqrk,sppmi,wwr,dnj,oskly,kny,wgpxd,bamy]
constraints=[AtMostKInARow(2, dnj)]
crossing=[oskly,wwr]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_2_1_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
