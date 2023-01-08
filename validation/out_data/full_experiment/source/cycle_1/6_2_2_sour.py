from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
rzazt = Factor("rzazt", ["yfjy", "qcomsb"])
mfxmh = Factor("mfxmh", ["njui", "kbdq"])
lejbn = Factor("lejbn", ["yfjy", "qcomsb"])
yseb = Factor("yseb", ["njui", "kbdq"])
skpifo = Factor("skpifo", ["syy", "pvbing"])
dfaag = Factor("dfaag", ["mtd", "zma"])
def awnll (dfaag, mfxmh):
    return dfaag == mfxmh
def lelm (dfaag, mfxmh):
    return not awnll(dfaag, mfxmh)
yrx = Factor("yrx", [DerivedLevel("uam", WithinTrial(awnll, [dfaag, mfxmh])), DerivedLevel("pbcmbd", WithinTrial(lelm, [dfaag, mfxmh]))])
def iqt (yseb, lejbn):
    return yseb == lejbn
def kxjuu (yseb, lejbn):
    return not iqt(yseb, lejbn)
sgguq = Factor("sgguq", [DerivedLevel("zsknwg", WithinTrial(iqt, [yseb, lejbn])), DerivedLevel("xua", WithinTrial(kxjuu, [yseb, lejbn]))])
design=[yrx,sgguq,rzazt,mfxmh,lejbn,yseb,skpifo,dfaag]
constraints=[MinimumTrials(46),AtMostKInARow(3, dfaag)]
crossing=[lejbn,yseb]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_2_2_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
