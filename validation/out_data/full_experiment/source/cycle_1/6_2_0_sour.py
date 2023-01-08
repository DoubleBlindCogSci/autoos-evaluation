from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
vce = Factor("vce", ["lblh", "uer"])
nacsbx = Factor("nacsbx", ["dykns", "fhnvoo"])
nqydwt = Factor("nqydwt", ["lblh", "uer"])
nizx = Factor("nizx", ["dykns", "fhnvoo"])
qlbbhb = Factor("qlbbhb", ["grviw", "njrmn"])
mmbm = Factor("mmbm", ["fqzevn", "qstpt"])
def qfvl (nizx, mmbm):
    return nizx == mmbm
def iposdx (nizx, mmbm):
    return not qfvl(nizx, mmbm)
yayb = Factor("yayb", [DerivedLevel("uvqryf", WithinTrial(qfvl, [nizx, mmbm])), DerivedLevel("uaty", WithinTrial(iposdx, [nizx, mmbm]))])
def rgc (nqydwt, vce):
    return nqydwt == vce
def jxua (nqydwt, vce):
    return not rgc(nqydwt, vce)
wwukd = Factor("wwukd", [DerivedLevel("qrmzj", WithinTrial(rgc, [nqydwt, vce])), DerivedLevel("cvihx", WithinTrial(jxua, [nqydwt, vce]))])
design=[yayb,wwukd,vce,nacsbx,nqydwt,nizx,qlbbhb,mmbm]
constraints=None
crossing=[nqydwt,nacsbx]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_2_0_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
