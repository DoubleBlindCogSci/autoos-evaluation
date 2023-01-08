from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
edkiip = Factor("edkiip", ["ddtexz", "fecbd"])
mas = Factor("mas", ["zdqq", "chnyyz"])
erdzl = Factor("erdzl", ["ddtexz", "fecbd"])
odbrwn = Factor("odbrwn", ["zdqq", "chnyyz"])
egh = Factor("egh", ["oxg", "pbouw"])
ukmfq = Factor("ukmfq", ["lumokl", "rkahyg"])
def qfsm (ukmfq, mas):
    return ukmfq == mas
def eveixc (ukmfq, mas):
    return not qfsm(ukmfq, mas)
yhm = Factor("yhm", [DerivedLevel("jdmfqw", WithinTrial(qfsm, [ukmfq, mas])), DerivedLevel("det", WithinTrial(eveixc, [ukmfq, mas]))])
design=[yhm,edkiip,mas,erdzl,odbrwn,egh,ukmfq]
constraints=[ExactlyKInARow(3, odbrwn)]
crossing=[odbrwn,erdzl]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_1_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
