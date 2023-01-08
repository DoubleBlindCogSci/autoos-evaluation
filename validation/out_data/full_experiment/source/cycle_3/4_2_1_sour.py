from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
dcoelt = Factor("dcoelt", ["trehz", "wrla"])
wohi = Factor("wohi", ["kjz", "tnks"])
zhzxp = Factor("zhzxp", ["trehz", "wrla"])
bsp = Factor("bsp", ["kjz", "tnks"])
def rhs (dcoelt, wohi):
    return dcoelt == wohi
def zeshbx (dcoelt, wohi):
    return not rhs(dcoelt, wohi)
ryvm = Factor("ryvm", [DerivedLevel("mdvu", WithinTrial(rhs, [dcoelt, wohi])), DerivedLevel("sbgra", WithinTrial(zeshbx, [dcoelt, wohi]))])
def cin (zhzxp, bsp):
    return zhzxp == bsp
def drwqm (zhzxp, bsp):
    return not cin(zhzxp, bsp)
uzbpmj = Factor("uzbpmj", [DerivedLevel("ehyn", WithinTrial(cin, [zhzxp, bsp])), DerivedLevel("vslmq", WithinTrial(drwqm, [zhzxp, bsp]))])
design=[ryvm,uzbpmj,dcoelt,wohi,zhzxp,bsp]
constraints=[MinimumTrials(45)]
crossing=[dcoelt,zhzxp]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_1_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
