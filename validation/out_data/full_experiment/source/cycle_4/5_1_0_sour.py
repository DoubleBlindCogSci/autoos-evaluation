from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
emmn = Factor("emmn", ["zfeun", "ulfa"])
qoz = Factor("qoz", ["zoe", "qdaza"])
upqhqx = Factor("upqhqx", ["zfeun", "ulfa"])
gvpmo = Factor("gvpmo", ["zoe", "qdaza"])
hdjam = Factor("hdjam", ["uhe", "oulgv"])
def xjhmo (gvpmo, qoz):
    return gvpmo == qoz
def ieja (gvpmo, qoz):
    return not xjhmo(gvpmo, qoz)
qus = Factor("qus", [DerivedLevel("mwsa", WithinTrial(xjhmo, [gvpmo, qoz])), DerivedLevel("oocxp", WithinTrial(ieja, [gvpmo, qoz]))])
design=[qus,emmn,qoz,upqhqx,gvpmo,hdjam]
constraints=[]
crossing=[qoz,hdjam]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_0_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
