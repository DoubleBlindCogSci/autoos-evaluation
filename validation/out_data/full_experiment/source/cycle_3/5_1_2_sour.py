from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
mhwfb = Factor("mhwfb", ["nqfkbi", "hvatw"])
xdpvuw = Factor("xdpvuw", ["xmkm", "mbz"])
jtlrt = Factor("jtlrt", ["nqfkbi", "hvatw"])
ior = Factor("ior", ["xmkm", "mbz"])
nhulxc = Factor("nhulxc", ["ffqhy", "ydycxv"])
def brpyxa (xdpvuw, jtlrt):
    return xdpvuw == jtlrt
def lfwe (xdpvuw, jtlrt):
    return not brpyxa(xdpvuw, jtlrt)
mps = Factor("mps", [DerivedLevel("yunbbk", WithinTrial(brpyxa, [xdpvuw, jtlrt])), DerivedLevel("gpiev", WithinTrial(lfwe, [xdpvuw, jtlrt]))])
design=[mps,mhwfb,xdpvuw,jtlrt,ior,nhulxc]
constraints=[MinimumTrials(26),AtMostKInARow(4, mhwfb)]
crossing=[xdpvuw,mps]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_2_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
