from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
vipu = Factor("vipu", ["nqaj", "fftz"])
pfl = Factor("pfl", ["vyo", "xkgy"])
nshhcw = Factor("nshhcw", ["nqaj", "fftz"])
bwmn = Factor("bwmn", ["vyo", "xkgy"])
def wtml (bwmn, nshhcw):
    return bwmn == nshhcw
def szk (bwmn, nshhcw):
    return not wtml(bwmn, nshhcw)
yic = Factor("yic", [DerivedLevel("guxkbh", WithinTrial(wtml, [bwmn, nshhcw])), DerivedLevel("wekqv", WithinTrial(szk, [bwmn, nshhcw]))])
def tozk (pfl, vipu):
    return pfl == vipu
def fwwj (pfl, vipu):
    return not tozk(pfl, vipu)
sxt = Factor("sxt", [DerivedLevel("pzruw", WithinTrial(tozk, [pfl, vipu])), DerivedLevel("mcsdum", WithinTrial(fwwj, [pfl, vipu]))])
design=[yic,sxt,vipu,pfl,nshhcw,bwmn]
constraints=[]
crossing=[pfl,bwmn]
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
