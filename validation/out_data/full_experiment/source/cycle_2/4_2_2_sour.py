from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
nzn = Factor("nzn", ["nvvtv", "patw"])
slm = Factor("slm", ["boga", "flif"])
qaufq = Factor("qaufq", ["nvvtv", "patw"])
uzqpl = Factor("uzqpl", ["boga", "flif"])
def uqx (slm, qaufq):
    return slm == qaufq
def ygekhj (slm, qaufq):
    return not uqx(slm, qaufq)
ehzalf = Factor("ehzalf", [DerivedLevel("bsigle", WithinTrial(uqx, [slm, qaufq])), DerivedLevel("hbc", WithinTrial(ygekhj, [slm, qaufq]))])
def xjekg (uzqpl, nzn):
    return uzqpl == nzn
def pvfxh (uzqpl, nzn):
    return not xjekg(uzqpl, nzn)
jxh = Factor("jxh", [DerivedLevel("safm", WithinTrial(xjekg, [uzqpl, nzn])), DerivedLevel("byfhj", WithinTrial(pvfxh, [uzqpl, nzn]))])
design=[ehzalf,jxh,nzn,slm,qaufq,uzqpl]
constraints=[AtLeastKInARow(4, qaufq),MinimumTrials(15)]
crossing=[jxh,ehzalf]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_2_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
