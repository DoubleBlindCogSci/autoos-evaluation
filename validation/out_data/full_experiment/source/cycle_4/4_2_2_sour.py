from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
uwlh = Factor("uwlh", ["hhs", "ptiktj"])
uza = Factor("uza", ["uiq", "tmxav"])
bog = Factor("bog", ["hhs", "ptiktj"])
boh = Factor("boh", ["uiq", "tmxav"])
def sgnyq (uwlh, boh):
    return uwlh == boh
def rqq (uwlh, boh):
    return not sgnyq(uwlh, boh)
znx = Factor("znx", [DerivedLevel("yjafe", WithinTrial(sgnyq, [uwlh, boh])), DerivedLevel("kndf", WithinTrial(rqq, [uwlh, boh]))])
def rmxdxd (uza, bog):
    return uza == bog
def bkeh (uza, bog):
    return not rmxdxd(uza, bog)
dupc = Factor("dupc", [DerivedLevel("duyj", WithinTrial(rmxdxd, [uza, bog])), DerivedLevel("ffiokh", WithinTrial(bkeh, [uza, bog]))])
design=[znx,dupc,uwlh,uza,bog,boh]
constraints=[AtLeastKInARow(3, znx),ExactlyKInARow(3, boh)]
crossing=[bog,uza]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_2_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
