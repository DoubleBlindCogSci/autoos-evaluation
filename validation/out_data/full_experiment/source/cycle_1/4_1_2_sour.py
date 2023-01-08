from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
lno = Factor("lno", ["sudp", "nogr"])
tula = Factor("tula", ["bkcad", "cjm"])
ygadz = Factor("ygadz", ["sudp", "nogr"])
qxlh = Factor("qxlh", ["bkcad", "cjm"])
def dcbt (tula, lno):
    return tula == lno
def ygvz (tula, lno):
    return not dcbt(tula, lno)
xkx = Factor("xkx", [DerivedLevel("ezcq", WithinTrial(dcbt, [tula, lno])), DerivedLevel("wgybo", WithinTrial(ygvz, [tula, lno]))])
design=[xkx,lno,tula,ygadz,qxlh]
constraints=[MinimumTrials(28),AtLeastKInARow(3, tula)]
crossing=[qxlh,xkx]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_1_2_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
