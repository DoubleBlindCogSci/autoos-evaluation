from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
oxt = Factor("oxt", ["sivho", "cqbgic"])
jvg = Factor("jvg", ["ohs", "wpyrc"])
moskvk = Factor("moskvk", ["sivho", "cqbgic"])
ijmr = Factor("ijmr", ["ohs", "wpyrc"])
def mlbfmb (ijmr, moskvk):
    return ijmr == moskvk
def zuegl (ijmr, moskvk):
    return not mlbfmb(ijmr, moskvk)
knmejn = Factor("knmejn", [DerivedLevel("dhmqoa", WithinTrial(mlbfmb, [ijmr, moskvk])), DerivedLevel("tgtul", WithinTrial(zuegl, [ijmr, moskvk]))])
def njsh (oxt, jvg):
    return oxt == jvg
def apbpic (oxt, jvg):
    return not njsh(oxt, jvg)
imxuu = Factor("imxuu", [DerivedLevel("ajirpt", WithinTrial(njsh, [oxt, jvg])), DerivedLevel("nozlj", WithinTrial(apbpic, [oxt, jvg]))])
design=[knmejn,imxuu,oxt,jvg,moskvk,ijmr]
constraints=[AtMostKInARow(2, oxt)]
crossing=[moskvk,oxt]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_1_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
