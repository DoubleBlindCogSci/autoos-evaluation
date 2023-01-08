from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
kwvw = Factor("kwvw", ["ltprq", "busur"])
vsgmy = Factor("vsgmy", ["dry", "affc"])
muv = Factor("muv", ["ltprq", "busur"])
pdajd = Factor("pdajd", ["dry", "affc"])
def sqrsgs (vsgmy, pdajd):
    return vsgmy == pdajd
def wol (vsgmy, pdajd):
    return not sqrsgs(vsgmy, pdajd)
rlhkr = Factor("rlhkr", [DerivedLevel("heml", WithinTrial(sqrsgs, [vsgmy, pdajd])), DerivedLevel("cepv", WithinTrial(wol, [vsgmy, pdajd]))])
def rpmiok (muv, kwvw):
    return muv == kwvw
def farn (muv, kwvw):
    return not rpmiok(muv, kwvw)
tkkanm = Factor("tkkanm", [DerivedLevel("qgxcm", WithinTrial(rpmiok, [muv, kwvw])), DerivedLevel("ggwik", WithinTrial(farn, [muv, kwvw]))])
design=[rlhkr,tkkanm,kwvw,vsgmy,muv,pdajd]
constraints=[ExactlyKInARow(2, vsgmy),AtMostKInARow(2, pdajd)]
crossing=[vsgmy,tkkanm]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_2_2_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
