from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
vshu = Factor("vshu", ["delb", "yzyt"])
xekqc = Factor("xekqc", ["zdxu", "ydd"])
xnffn = Factor("xnffn", ["delb", "yzyt"])
dpfsnj = Factor("dpfsnj", ["zdxu", "ydd"])
tpuh = Factor("tpuh", ["dtr", "luunw"])
def vjm (dpfsnj, tpuh):
    return dpfsnj == tpuh
def inony (dpfsnj, tpuh):
    return not vjm(dpfsnj, tpuh)
uqdkg = Factor("uqdkg", [DerivedLevel("jxmnij", WithinTrial(vjm, [dpfsnj, tpuh])), DerivedLevel("hutd", WithinTrial(inony, [dpfsnj, tpuh]))])
design=[uqdkg,vshu,xekqc,xnffn,dpfsnj,tpuh]
constraints=[AtMostKInARow(4, uqdkg)]
crossing=[vshu,tpuh]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_1_1_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
