from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
rdofu = Factor("rdofu", ["pyobz", "ofkrum"])
knakml = Factor("knakml", ["qubuk", "dok"])
qnpxs = Factor("qnpxs", ["pyobz", "ofkrum"])
vwpw = Factor("vwpw", ["qubuk", "dok"])
dyti = Factor("dyti", ["hpcxbk", "nfp"])
def lfncx (knakml, dyti):
    return knakml == dyti
def eucmp (knakml, dyti):
    return not lfncx(knakml, dyti)
qad = Factor("qad", [DerivedLevel("iast", WithinTrial(lfncx, [knakml, dyti])), DerivedLevel("mlsvfv", WithinTrial(eucmp, [knakml, dyti]))])
def obcrob (vwpw, rdofu):
    return vwpw == rdofu
def woq (vwpw, rdofu):
    return not obcrob(vwpw, rdofu)
kho = Factor("kho", [DerivedLevel("eedltm", WithinTrial(obcrob, [vwpw, rdofu])), DerivedLevel("ived", WithinTrial(woq, [vwpw, rdofu]))])
design=[qad,kho,rdofu,knakml,qnpxs,vwpw,dyti]
constraints=[]
crossing=[kho,vwpw]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_0_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
