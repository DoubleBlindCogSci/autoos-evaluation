from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
dtr = Factor("dtr", ["ted", "rqhh"])
wlgsw = Factor("wlgsw", ["pbvh", "zkbz"])
pfj = Factor("pfj", ["ted", "rqhh"])
hbkma = Factor("hbkma", ["pbvh", "zkbz"])
lhe = Factor("lhe", ["dihh", "fpmzkq"])
def ywhf (dtr, pfj):
    return dtr == pfj
def irebb (dtr, pfj):
    return not ywhf(dtr, pfj)
sovpx = Factor("sovpx", [DerivedLevel("xfxluk", WithinTrial(ywhf, [dtr, pfj])), DerivedLevel("qmrrzn", WithinTrial(irebb, [dtr, pfj]))])
design=[sovpx,dtr,wlgsw,pfj,hbkma,lhe]
constraints=[]
crossing=[wlgsw,sovpx]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_0_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
