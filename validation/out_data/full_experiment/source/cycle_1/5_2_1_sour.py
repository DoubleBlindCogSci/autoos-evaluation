from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
mojan = Factor("mojan", ["nwu", "psksh"])
odmmgw = Factor("odmmgw", ["gji", "vois"])
xbk = Factor("xbk", ["nwu", "psksh"])
kvkn = Factor("kvkn", ["gji", "vois"])
pypwky = Factor("pypwky", ["rmnym", "pthd"])
def flzpm (mojan, odmmgw):
    return mojan == odmmgw
def iopgqj (mojan, odmmgw):
    return not flzpm(mojan, odmmgw)
qsms = Factor("qsms", [DerivedLevel("czo", WithinTrial(flzpm, [mojan, odmmgw])), DerivedLevel("ohxl", WithinTrial(iopgqj, [mojan, odmmgw]))])
def kxfddw (xbk, pypwky):
    return xbk == pypwky
def dxjlog (xbk, pypwky):
    return not kxfddw(xbk, pypwky)
jlt = Factor("jlt", [DerivedLevel("szftzq", WithinTrial(kxfddw, [xbk, pypwky])), DerivedLevel("ncfc", WithinTrial(dxjlog, [xbk, pypwky]))])
design=[qsms,jlt,mojan,odmmgw,xbk,kvkn,pypwky]
constraints=[AtMostKInARow(4, qsms)]
crossing=[jlt,qsms]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_2_1_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
