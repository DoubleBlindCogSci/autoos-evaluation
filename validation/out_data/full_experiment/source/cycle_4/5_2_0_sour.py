from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
mrgf = Factor("mrgf", ["fsvan", "nie"])
icswhs = Factor("icswhs", ["llcpvl", "wchnv"])
xrzgp = Factor("xrzgp", ["fsvan", "nie"])
imlvth = Factor("imlvth", ["llcpvl", "wchnv"])
nrf = Factor("nrf", ["rlwwkc", "qoakhq"])
def hrw (mrgf, xrzgp):
    return mrgf == xrzgp
def hqty (mrgf, xrzgp):
    return not hrw(mrgf, xrzgp)
obg = Factor("obg", [DerivedLevel("gpqi", WithinTrial(hrw, [mrgf, xrzgp])), DerivedLevel("kfpob", WithinTrial(hqty, [mrgf, xrzgp]))])
def hnhm (nrf, imlvth):
    return nrf == imlvth
def tyfmtz (nrf, imlvth):
    return not hnhm(nrf, imlvth)
jvks = Factor("jvks", [DerivedLevel("fhdlv", WithinTrial(hnhm, [nrf, imlvth])), DerivedLevel("gwvvx", WithinTrial(tyfmtz, [nrf, imlvth]))])
design=[obg,jvks,mrgf,icswhs,xrzgp,imlvth,nrf]
constraints=[]
crossing=[jvks,obg]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_0_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
