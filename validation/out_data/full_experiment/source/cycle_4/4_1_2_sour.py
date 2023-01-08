from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
hpocc = Factor("hpocc", ["xqvh", "ppja"])
yljkz = Factor("yljkz", ["aua", "yrdzt"])
eppi = Factor("eppi", ["xqvh", "ppja"])
rkfb = Factor("rkfb", ["aua", "yrdzt"])
def wgh (yljkz, eppi):
    return yljkz == eppi
def lgdqp (yljkz, eppi):
    return not wgh(yljkz, eppi)
bft = Factor("bft", [DerivedLevel("sxhbt", WithinTrial(wgh, [yljkz, eppi])), DerivedLevel("bzmddf", WithinTrial(lgdqp, [yljkz, eppi]))])
design=[bft,hpocc,yljkz,eppi,rkfb]
constraints=[AtLeastKInARow(4, yljkz),ExactlyKInARow(2, yljkz)]
crossing=[yljkz,bft]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_2_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
