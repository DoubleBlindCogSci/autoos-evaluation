from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
toll = Factor("toll", ["nqwgeu", "wwudy"])
pkkm = Factor("pkkm", ["khun", "bkyhp"])
hhizte = Factor("hhizte", ["nqwgeu", "wwudy"])
rhl = Factor("rhl", ["khun", "bkyhp"])
def bpae (rhl, hhizte):
    return rhl == hhizte
def ygh (rhl, hhizte):
    return not bpae(rhl, hhizte)
cwh = Factor("cwh", [DerivedLevel("zdljt", WithinTrial(bpae, [rhl, hhizte])), DerivedLevel("blukz", WithinTrial(ygh, [rhl, hhizte]))])
def lfaj (pkkm, toll):
    return pkkm == toll
def sml (pkkm, toll):
    return not lfaj(pkkm, toll)
hnt = Factor("hnt", [DerivedLevel("rjvf", WithinTrial(lfaj, [pkkm, toll])), DerivedLevel("qoemb", WithinTrial(sml, [pkkm, toll]))])
design=[cwh,hnt,toll,pkkm,hhizte,rhl]
constraints=[MinimumTrials(36),AtLeastKInARow(4, hhizte)]
crossing=[toll,hhizte]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_2_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
