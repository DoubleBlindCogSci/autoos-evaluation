from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
vkjko = Factor("vkjko", ["fga", "pdoq"])
wgrgtc = Factor("wgrgtc", ["bbwayz", "tmthev"])
wewe = Factor("wewe", ["fga", "pdoq"])
jkhd = Factor("jkhd", ["bbwayz", "tmthev"])
oir = Factor("oir", ["bjpq", "sfjahf"])
def mqob (oir, jkhd):
    return oir == jkhd
def ubgfkw (oir, jkhd):
    return not mqob(oir, jkhd)
eivlb = Factor("eivlb", [DerivedLevel("irho", WithinTrial(mqob, [oir, jkhd])), DerivedLevel("hjbpis", WithinTrial(ubgfkw, [oir, jkhd]))])
design=[eivlb,vkjko,wgrgtc,wewe,jkhd,oir]
constraints=[MinimumTrials(26)]
crossing=[wgrgtc,eivlb]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_1_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
