from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
qwm = Factor("qwm", ["dfyept", "pfaqzf"])
qgau = Factor("qgau", ["ljmk", "bajuw"])
vztzuw = Factor("vztzuw", ["dfyept", "pfaqzf"])
upvxq = Factor("upvxq", ["ljmk", "bajuw"])
ykfncu = Factor("ykfncu", ["uzoatr", "ocup"])
def zswjux (qwm, upvxq):
    return qwm == upvxq
def wkfx (qwm, upvxq):
    return not zswjux(qwm, upvxq)
zklvsn = Factor("zklvsn", [DerivedLevel("dxvrh", WithinTrial(zswjux, [qwm, upvxq])), DerivedLevel("rxalmf", WithinTrial(wkfx, [qwm, upvxq]))])
def aqclgk (vztzuw, qgau):
    return vztzuw == qgau
def fdchco (vztzuw, qgau):
    return not aqclgk(vztzuw, qgau)
swopp = Factor("swopp", [DerivedLevel("airucu", WithinTrial(aqclgk, [vztzuw, qgau])), DerivedLevel("ekoc", WithinTrial(fdchco, [vztzuw, qgau]))])
design=[zklvsn,swopp,qwm,qgau,vztzuw,upvxq,ykfncu]
constraints=None
crossing=[ykfncu,vztzuw]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_2_0_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
