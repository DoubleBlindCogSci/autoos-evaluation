from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
dfqk = Factor("dfqk", ["psdz", "flwj"])
ptzx = Factor("ptzx", ["xhsut", "zgap"])
jyg = Factor("jyg", ["psdz", "flwj"])
gqdbe = Factor("gqdbe", ["xhsut", "zgap"])
xgijm = Factor("xgijm", ["swu", "jdvb"])
zlvm = Factor("zlvm", ["fxydov", "qqc"])
def wlyd (xgijm, zlvm):
    return xgijm == zlvm
def qsnv (xgijm, zlvm):
    return not wlyd(xgijm, zlvm)
jczjok = Factor("jczjok", [DerivedLevel("hsh", WithinTrial(wlyd, [xgijm, zlvm])), DerivedLevel("eik", WithinTrial(qsnv, [xgijm, zlvm]))])
design=[jczjok,dfqk,ptzx,jyg,gqdbe,xgijm,zlvm]
constraints=[ExactlyKInARow(3, zlvm),MinimumTrials(52)]
crossing=[xgijm,dfqk]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_1_2_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
