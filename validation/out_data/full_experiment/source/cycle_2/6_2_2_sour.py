from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
cxac = Factor("cxac", ["alpai", "mdiei"])
byvob = Factor("byvob", ["juc", "bzdi"])
ayfgq = Factor("ayfgq", ["alpai", "mdiei"])
tnd = Factor("tnd", ["juc", "bzdi"])
uwgbrp = Factor("uwgbrp", ["gnyajh", "bqg"])
phb = Factor("phb", ["mjyfwo", "jea"])
def mls (phb, uwgbrp):
    return phb == uwgbrp
def dcczs (phb, uwgbrp):
    return not mls(phb, uwgbrp)
funv = Factor("funv", [DerivedLevel("jrhlqv", WithinTrial(mls, [phb, uwgbrp])), DerivedLevel("axyuo", WithinTrial(dcczs, [phb, uwgbrp]))])
def poa (cxac, tnd):
    return cxac == tnd
def kmfob (cxac, tnd):
    return not poa(cxac, tnd)
bkcnhy = Factor("bkcnhy", [DerivedLevel("cfae", WithinTrial(poa, [cxac, tnd])), DerivedLevel("ljbbi", WithinTrial(kmfob, [cxac, tnd]))])
design=[funv,bkcnhy,cxac,byvob,ayfgq,tnd,uwgbrp,phb]
constraints=[AtLeastKInARow(3, byvob),AtMostKInARow(4, uwgbrp)]
crossing=[cxac,byvob]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_2_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
