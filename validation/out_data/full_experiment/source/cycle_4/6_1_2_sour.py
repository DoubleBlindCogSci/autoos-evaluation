from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
snat = Factor("snat", ["pkijs", "krrj"])
kaqka = Factor("kaqka", ["inqo", "qggwd"])
lvisj = Factor("lvisj", ["pkijs", "krrj"])
gqw = Factor("gqw", ["inqo", "qggwd"])
wkqe = Factor("wkqe", ["cpar", "pcfsm"])
pyoyje = Factor("pyoyje", ["yejf", "aupzma"])
def fdr (lvisj, pyoyje):
    return lvisj == pyoyje
def euiuag (lvisj, pyoyje):
    return not fdr(lvisj, pyoyje)
hjip = Factor("hjip", [DerivedLevel("tutcm", WithinTrial(fdr, [lvisj, pyoyje])), DerivedLevel("micqz", WithinTrial(euiuag, [lvisj, pyoyje]))])
design=[hjip,snat,kaqka,lvisj,gqw,wkqe,pyoyje]
constraints=[ExactlyKInARow(4, wkqe),AtMostKInARow(2, snat)]
crossing=[kaqka,hjip]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_2_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
