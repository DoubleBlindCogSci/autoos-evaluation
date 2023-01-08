from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
gqw = Factor("gqw", ["ohpe", "rbclng"])
wdp = Factor("wdp", ["eioqw", "rrvin"])
nrbavq = Factor("nrbavq", ["ohpe", "rbclng"])
xlpll = Factor("xlpll", ["eioqw", "rrvin"])
xne = Factor("xne", ["erjk", "yow"])
cee = Factor("cee", ["yqzavs", "gof"])
def rofz (nrbavq, wdp):
    return nrbavq == wdp
def yfsv (nrbavq, wdp):
    return not rofz(nrbavq, wdp)
zzsf = Factor("zzsf", [DerivedLevel("cmjwd", WithinTrial(rofz, [nrbavq, wdp])), DerivedLevel("yffeb", WithinTrial(yfsv, [nrbavq, wdp]))])
design=[zzsf,gqw,wdp,nrbavq,xlpll,xne,cee]
constraints=[MinimumTrials(39)]
crossing=[nrbavq,cee]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_1_1_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
