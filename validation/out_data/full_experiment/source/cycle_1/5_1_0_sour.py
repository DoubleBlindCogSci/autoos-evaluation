from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
kxk = Factor("kxk", ["nllpb", "nhg"])
oqba = Factor("oqba", ["bdalt", "xjsf"])
voo = Factor("voo", ["nllpb", "nhg"])
wtq = Factor("wtq", ["bdalt", "xjsf"])
isf = Factor("isf", ["lavu", "tqntet"])
def jeghv (voo, oqba):
    return voo == oqba
def tadi (voo, oqba):
    return not jeghv(voo, oqba)
vceeea = Factor("vceeea", [DerivedLevel("rpds", WithinTrial(jeghv, [voo, oqba])), DerivedLevel("rth", WithinTrial(tadi, [voo, oqba]))])
design=[vceeea,kxk,oqba,voo,wtq,isf]
constraints=None
crossing=[kxk,voo]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_1_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_1_0_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
