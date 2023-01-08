from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
loslz = Factor("loslz", ["acnxo", "igqh"])
odd = Factor("odd", ["bojkc", "phe"])
mefc = Factor("mefc", ["acnxo", "igqh"])
hkki = Factor("hkki", ["bojkc", "phe"])
oju = Factor("oju", ["vsw", "xfg"])
def sko (oju, hkki):
    return oju == hkki
def ynim (oju, hkki):
    return not sko(oju, hkki)
djawfc = Factor("djawfc", [DerivedLevel("clt", WithinTrial(sko, [oju, hkki])), DerivedLevel("pkadp", WithinTrial(ynim, [oju, hkki]))])
design=[djawfc,loslz,odd,mefc,hkki,oju]
constraints=[MinimumTrials(27),AtLeastKInARow(4, mefc)]
crossing=[djawfc,hkki]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_1_2_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
