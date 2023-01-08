from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
dodd = Factor("dodd", ["lfk", "qsy"])
vodhe = Factor("vodhe", ["tkttub", "rfctx"])
fnv = Factor("fnv", ["lfk", "qsy"])
fiw = Factor("fiw", ["tkttub", "rfctx"])
def kcv (dodd, fiw):
    return dodd == fiw
def ork (dodd, fiw):
    return not kcv(dodd, fiw)
dvx = Factor("dvx", [DerivedLevel("ylij", WithinTrial(kcv, [dodd, fiw])), DerivedLevel("gya", WithinTrial(ork, [dodd, fiw]))])
design=[dvx,dodd,vodhe,fnv,fiw]
constraints=[AtMostKInARow(4, dodd)]
crossing=[fiw,dodd]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_1_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
