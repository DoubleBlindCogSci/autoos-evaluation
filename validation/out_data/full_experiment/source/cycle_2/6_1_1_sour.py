from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
kqslu = Factor("kqslu", ["famp", "cmff"])
kjt = Factor("kjt", ["uhoqoh", "aazgln"])
trysn = Factor("trysn", ["famp", "cmff"])
dbp = Factor("dbp", ["uhoqoh", "aazgln"])
miayr = Factor("miayr", ["rfddz", "tth"])
hdrgrk = Factor("hdrgrk", ["wbesla", "kknw"])
def zkjbd (kjt, dbp):
    return kjt == dbp
def bsycn (kjt, dbp):
    return not zkjbd(kjt, dbp)
xdaerc = Factor("xdaerc", [DerivedLevel("ddfx", WithinTrial(zkjbd, [kjt, dbp])), DerivedLevel("retip", WithinTrial(bsycn, [kjt, dbp]))])
design=[xdaerc,kqslu,kjt,trysn,dbp,miayr,hdrgrk]
constraints=[AtLeastKInARow(4, dbp)]
crossing=[kjt,xdaerc]
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
