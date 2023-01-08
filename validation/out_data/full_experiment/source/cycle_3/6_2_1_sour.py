from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
avbwpg = Factor("avbwpg", ["cimg", "hbfe"])
xzx = Factor("xzx", ["fsk", "nnbtc"])
qrtckt = Factor("qrtckt", ["cimg", "hbfe"])
zomk = Factor("zomk", ["fsk", "nnbtc"])
dergv = Factor("dergv", ["sxzdej", "rxwuo"])
ubzdcu = Factor("ubzdcu", ["vdom", "mqg"])
def jhy (xzx, ubzdcu):
    return xzx == ubzdcu
def zjigs (xzx, ubzdcu):
    return not jhy(xzx, ubzdcu)
ftmaw = Factor("ftmaw", [DerivedLevel("nch", WithinTrial(jhy, [xzx, ubzdcu])), DerivedLevel("mfdpop", WithinTrial(zjigs, [xzx, ubzdcu]))])
def lomu (qrtckt, dergv):
    return qrtckt == dergv
def rycyc (qrtckt, dergv):
    return not lomu(qrtckt, dergv)
upva = Factor("upva", [DerivedLevel("gukug", WithinTrial(lomu, [qrtckt, dergv])), DerivedLevel("bseu", WithinTrial(rycyc, [qrtckt, dergv]))])
design=[ftmaw,upva,avbwpg,xzx,qrtckt,zomk,dergv,ubzdcu]
constraints=[MinimumTrials(29)]
crossing=[dergv,zomk]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_2_1_0.csv"))
nr_regular=6
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
