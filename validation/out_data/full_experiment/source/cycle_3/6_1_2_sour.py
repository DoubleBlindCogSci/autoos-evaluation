from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
kgx = Factor("kgx", ["rxrgv", "xdqhc"])
ujbe = Factor("ujbe", ["jaehg", "gmnopl"])
cbiwgn = Factor("cbiwgn", ["rxrgv", "xdqhc"])
tqlnk = Factor("tqlnk", ["jaehg", "gmnopl"])
pdhel = Factor("pdhel", ["hpziox", "wisqo"])
sfe = Factor("sfe", ["nep", "oqcus"])
def lgu (pdhel, ujbe):
    return pdhel == ujbe
def mxuj (pdhel, ujbe):
    return not lgu(pdhel, ujbe)
latl = Factor("latl", [DerivedLevel("dgcdsk", WithinTrial(lgu, [pdhel, ujbe])), DerivedLevel("zxrpht", WithinTrial(mxuj, [pdhel, ujbe]))])
design=[latl,kgx,ujbe,cbiwgn,tqlnk,pdhel,sfe]
constraints=[AtMostKInARow(2, sfe),AtLeastKInARow(2, ujbe)]
crossing=[cbiwgn,latl]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_2_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
