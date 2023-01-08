from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
yvt = Factor("yvt", ["aspg", "mypy"])
nwy = Factor("nwy", ["ludty", "sniosf"])
shy = Factor("shy", ["aspg", "mypy"])
yvnfyr = Factor("yvnfyr", ["ludty", "sniosf"])
eqhnnb = Factor("eqhnnb", ["xjf", "oxjjzy"])
def jwc (eqhnnb, yvt):
    return eqhnnb == yvt
def msqcoq (eqhnnb, yvt):
    return not jwc(eqhnnb, yvt)
cdf = Factor("cdf", [DerivedLevel("rprpk", WithinTrial(jwc, [eqhnnb, yvt])), DerivedLevel("zydsnt", WithinTrial(msqcoq, [eqhnnb, yvt]))])
design=[cdf,yvt,nwy,shy,yvnfyr,eqhnnb]
constraints=[AtMostKInARow(4, yvt),MinimumTrials(32)]
crossing=[yvt,yvnfyr]
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
