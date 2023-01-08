from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
ozffyg = Factor("ozffyg", ["ktpg", "ezgdye"])
eor = Factor("eor", ["bvwt", "odzvfn"])
ulmvu = Factor("ulmvu", ["ktpg", "ezgdye"])
ydyizj = Factor("ydyizj", ["bvwt", "odzvfn"])
def vyt (eor, ydyizj):
    return eor == ydyizj
def zfu (eor, ydyizj):
    return not vyt(eor, ydyizj)
vnud = Factor("vnud", [DerivedLevel("cmru", WithinTrial(vyt, [eor, ydyizj])), DerivedLevel("hjfu", WithinTrial(zfu, [eor, ydyizj]))])
design=[vnud,ozffyg,eor,ulmvu,ydyizj]
constraints=[AtMostKInARow(3, vnud)]
crossing=[ulmvu,vnud]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_1_1_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
