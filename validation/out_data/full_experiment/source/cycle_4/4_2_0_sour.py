from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
npfih = Factor("npfih", ["zqc", "szrkc"])
ldtn = Factor("ldtn", ["eqq", "mcuj"])
olhm = Factor("olhm", ["zqc", "szrkc"])
vac = Factor("vac", ["eqq", "mcuj"])
def tuqne (olhm, npfih):
    return olhm == npfih
def lopnc (olhm, npfih):
    return not tuqne(olhm, npfih)
rnm = Factor("rnm", [DerivedLevel("zsrr", WithinTrial(tuqne, [olhm, npfih])), DerivedLevel("ebnz", WithinTrial(lopnc, [olhm, npfih]))])
def eofmvl (vac, ldtn):
    return vac == ldtn
def vxcr (vac, ldtn):
    return not eofmvl(vac, ldtn)
oelqby = Factor("oelqby", [DerivedLevel("njfk", WithinTrial(eofmvl, [vac, ldtn])), DerivedLevel("oaiui", WithinTrial(vxcr, [vac, ldtn]))])
design=[rnm,oelqby,npfih,ldtn,olhm,vac]
constraints=[]
crossing=[ldtn,olhm]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
