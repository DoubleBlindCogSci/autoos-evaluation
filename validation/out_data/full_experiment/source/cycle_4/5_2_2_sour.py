from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
ihaxo = Factor("ihaxo", ["nebj", "gqov"])
mwabx = Factor("mwabx", ["upfna", "qnn"])
drfsq = Factor("drfsq", ["nebj", "gqov"])
wwviw = Factor("wwviw", ["upfna", "qnn"])
ddx = Factor("ddx", ["oesdd", "cgcxdg"])
def rkif (wwviw, ddx):
    return wwviw == ddx
def dmlds (wwviw, ddx):
    return not rkif(wwviw, ddx)
mehm = Factor("mehm", [DerivedLevel("onat", WithinTrial(rkif, [wwviw, ddx])), DerivedLevel("zbtzh", WithinTrial(dmlds, [wwviw, ddx]))])
def xjcy (drfsq, ihaxo):
    return drfsq == ihaxo
def hlh (drfsq, ihaxo):
    return not xjcy(drfsq, ihaxo)
trtz = Factor("trtz", [DerivedLevel("itvon", WithinTrial(xjcy, [drfsq, ihaxo])), DerivedLevel("cuvewk", WithinTrial(hlh, [drfsq, ihaxo]))])
design=[mehm,trtz,ihaxo,mwabx,drfsq,wwviw,ddx]
constraints=[ExactlyKInARow(3, trtz),AtLeastKInARow(2, trtz)]
crossing=[wwviw,trtz]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_2_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
