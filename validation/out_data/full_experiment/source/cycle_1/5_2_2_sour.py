from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
qbels = Factor("qbels", ["fedyp", "qvtee"])
zafcwt = Factor("zafcwt", ["jkyqe", "hvpzy"])
gkvi = Factor("gkvi", ["fedyp", "qvtee"])
kfzgby = Factor("kfzgby", ["jkyqe", "hvpzy"])
dpzavt = Factor("dpzavt", ["vnmzjk", "vpgjkg"])
def spegxs (kfzgby, gkvi):
    return kfzgby == gkvi
def fspbs (kfzgby, gkvi):
    return not spegxs(kfzgby, gkvi)
hwyre = Factor("hwyre", [DerivedLevel("zdvnk", WithinTrial(spegxs, [kfzgby, gkvi])), DerivedLevel("mxo", WithinTrial(fspbs, [kfzgby, gkvi]))])
def hoxtl (zafcwt, dpzavt):
    return zafcwt == dpzavt
def mkv (zafcwt, dpzavt):
    return not hoxtl(zafcwt, dpzavt)
dfznp = Factor("dfznp", [DerivedLevel("gkkww", WithinTrial(hoxtl, [zafcwt, dpzavt])), DerivedLevel("vxtxq", WithinTrial(mkv, [zafcwt, dpzavt]))])
design=[hwyre,dfznp,qbels,zafcwt,gkvi,kfzgby,dpzavt]
constraints=[ExactlyKInARow(3, qbels),AtLeastKInARow(4, kfzgby)]
crossing=[dfznp,zafcwt]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_2_2_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
