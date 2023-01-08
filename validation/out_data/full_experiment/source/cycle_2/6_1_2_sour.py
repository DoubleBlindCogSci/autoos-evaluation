from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
zuqn = Factor("zuqn", ["rqu", "yzh"])
iob = Factor("iob", ["wsep", "xvci"])
mdz = Factor("mdz", ["rqu", "yzh"])
hmoud = Factor("hmoud", ["wsep", "xvci"])
ibonqh = Factor("ibonqh", ["tyyna", "knxo"])
ktcou = Factor("ktcou", ["vwbsg", "wwqtz"])
def neuyip (zuqn, iob):
    return zuqn == iob
def drhy (zuqn, iob):
    return not neuyip(zuqn, iob)
hci = Factor("hci", [DerivedLevel("gzrsh", WithinTrial(neuyip, [zuqn, iob])), DerivedLevel("fbv", WithinTrial(drhy, [zuqn, iob]))])
design=[hci,zuqn,iob,mdz,hmoud,ibonqh,ktcou]
constraints=[ExactlyKInARow(4, mdz),AtLeastKInARow(2, zuqn)]
crossing=[mdz,hci]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_2_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
