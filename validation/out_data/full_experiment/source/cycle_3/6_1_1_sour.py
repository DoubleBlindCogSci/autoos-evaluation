from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
opstb = Factor("opstb", ["gizmm", "oaxg"])
hehx = Factor("hehx", ["ewbu", "vai"])
bob = Factor("bob", ["gizmm", "oaxg"])
pdwuqf = Factor("pdwuqf", ["ewbu", "vai"])
pyxfb = Factor("pyxfb", ["cohge", "tdm"])
iwhnba = Factor("iwhnba", ["vehu", "xmcl"])
def cghug (bob, pdwuqf):
    return bob == pdwuqf
def zdxjg (bob, pdwuqf):
    return not cghug(bob, pdwuqf)
niyyi = Factor("niyyi", [DerivedLevel("ieeoy", WithinTrial(cghug, [bob, pdwuqf])), DerivedLevel("wywxab", WithinTrial(zdxjg, [bob, pdwuqf]))])
design=[niyyi,opstb,hehx,bob,pdwuqf,pyxfb,iwhnba]
constraints=[AtLeastKInARow(4, opstb)]
crossing=[hehx,pyxfb]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_1_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
