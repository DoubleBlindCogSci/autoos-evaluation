from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
byds = Factor("byds", ["wnsa", "pbvws"])
zqhjpa = Factor("zqhjpa", ["auo", "ikosc"])
ppktzu = Factor("ppktzu", ["wnsa", "pbvws"])
bwci = Factor("bwci", ["auo", "ikosc"])
rxukub = Factor("rxukub", ["txxm", "yojoxb"])
def wzo (bwci, rxukub):
    return bwci == rxukub
def qgra (bwci, rxukub):
    return not wzo(bwci, rxukub)
cznezw = Factor("cznezw", [DerivedLevel("fzjgi", WithinTrial(wzo, [bwci, rxukub])), DerivedLevel("qpqg", WithinTrial(qgra, [bwci, rxukub]))])
def rbusy (byds, zqhjpa):
    return byds == zqhjpa
def zuzbhe (byds, zqhjpa):
    return not rbusy(byds, zqhjpa)
gabz = Factor("gabz", [DerivedLevel("grwuc", WithinTrial(rbusy, [byds, zqhjpa])), DerivedLevel("tysmu", WithinTrial(zuzbhe, [byds, zqhjpa]))])
design=[cznezw,gabz,byds,zqhjpa,ppktzu,bwci,rxukub]
constraints=[]
crossing=[byds,ppktzu]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_0_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
