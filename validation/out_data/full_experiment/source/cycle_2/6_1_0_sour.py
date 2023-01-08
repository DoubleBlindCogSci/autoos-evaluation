from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
aiq = Factor("aiq", ["dbjumx", "woafy"])
jefa = Factor("jefa", ["qkd", "zighty"])
leophp = Factor("leophp", ["dbjumx", "woafy"])
vwqn = Factor("vwqn", ["qkd", "zighty"])
zovw = Factor("zovw", ["qtjexx", "swxghh"])
qexm = Factor("qexm", ["ggxeg", "lbxnp"])
def ypkh (jefa, leophp):
    return jefa == leophp
def znu (jefa, leophp):
    return not ypkh(jefa, leophp)
pye = Factor("pye", [DerivedLevel("bqekyw", WithinTrial(ypkh, [jefa, leophp])), DerivedLevel("ygfjnn", WithinTrial(znu, [jefa, leophp]))])
design=[pye,aiq,jefa,leophp,vwqn,zovw,qexm]
constraints=[]
crossing=[vwqn,aiq]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_0_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
