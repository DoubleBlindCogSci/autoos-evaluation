from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
chrlaq = Factor("chrlaq", ["tdmy", "jevqi"])
fbxkr = Factor("fbxkr", ["brsx", "soct"])
iuqbla = Factor("iuqbla", ["tdmy", "jevqi"])
mozm = Factor("mozm", ["brsx", "soct"])
def stkcrb (mozm, iuqbla):
    return mozm == iuqbla
def qxk (mozm, iuqbla):
    return not stkcrb(mozm, iuqbla)
fjoa = Factor("fjoa", [DerivedLevel("icnyt", WithinTrial(stkcrb, [mozm, iuqbla])), DerivedLevel("ove", WithinTrial(qxk, [mozm, iuqbla]))])
design=[fjoa,chrlaq,fbxkr,iuqbla,mozm]
constraints=[AtMostKInARow(4, fjoa),ExactlyKInARow(4, fbxkr)]
crossing=[iuqbla,chrlaq]
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
