from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
crs = Factor("crs", ["pmg", "qkb"])
iaqirv = Factor("iaqirv", ["qvcp", "xxpwn"])
ivfjrc = Factor("ivfjrc", ["pmg", "qkb"])
auc = Factor("auc", ["qvcp", "xxpwn"])
def nkx (crs, auc):
    return crs == auc
def pwrq (crs, auc):
    return not nkx(crs, auc)
iuovx = Factor("iuovx", [DerivedLevel("nqlgn", WithinTrial(nkx, [crs, auc])), DerivedLevel("iaajvq", WithinTrial(pwrq, [crs, auc]))])
def pqq (iaqirv, ivfjrc):
    return iaqirv == ivfjrc
def qyit (iaqirv, ivfjrc):
    return not pqq(iaqirv, ivfjrc)
mrqv = Factor("mrqv", [DerivedLevel("uegs", WithinTrial(pqq, [iaqirv, ivfjrc])), DerivedLevel("hhguew", WithinTrial(qyit, [iaqirv, ivfjrc]))])
design=[iuovx,mrqv,crs,iaqirv,ivfjrc,auc]
constraints=[]
crossing=[mrqv,crs]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
