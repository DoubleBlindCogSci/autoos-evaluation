from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
ftg = Factor("ftg", ["nqxlo", "iqtp"])
cdt = Factor("cdt", ["pcm", "hqiju"])
wgrk = Factor("wgrk", ["nqxlo", "iqtp"])
buvqha = Factor("buvqha", ["pcm", "hqiju"])
def nfrrw (cdt, wgrk):
    return cdt == wgrk
def jvymc (cdt, wgrk):
    return not nfrrw(cdt, wgrk)
gcu = Factor("gcu", [DerivedLevel("wziqu", WithinTrial(nfrrw, [cdt, wgrk])), DerivedLevel("slbd", WithinTrial(jvymc, [cdt, wgrk]))])
design=[gcu,ftg,cdt,wgrk,buvqha]
constraints=[MinimumTrials(35),ExactlyKInARow(3, gcu)]
crossing=[ftg,gcu]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_1_2_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
