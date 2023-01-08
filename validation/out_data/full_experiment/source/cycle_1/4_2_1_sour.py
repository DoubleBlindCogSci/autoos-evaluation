from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
zzdmwj = Factor("zzdmwj", ["ioetr", "jlbmqt"])
gkn = Factor("gkn", ["ocdj", "ovk"])
evz = Factor("evz", ["ioetr", "jlbmqt"])
toiht = Factor("toiht", ["ocdj", "ovk"])
def etfev (evz, zzdmwj):
    return evz == zzdmwj
def vea (evz, zzdmwj):
    return not etfev(evz, zzdmwj)
khvnl = Factor("khvnl", [DerivedLevel("kknbk", WithinTrial(etfev, [evz, zzdmwj])), DerivedLevel("gebdr", WithinTrial(vea, [evz, zzdmwj]))])
def doyx (gkn, toiht):
    return gkn == toiht
def pgesuj (gkn, toiht):
    return not doyx(gkn, toiht)
fdan = Factor("fdan", [DerivedLevel("cjjghi", WithinTrial(doyx, [gkn, toiht])), DerivedLevel("urts", WithinTrial(pgesuj, [gkn, toiht]))])
design=[khvnl,fdan,zzdmwj,gkn,evz,toiht]
constraints=[AtLeastKInARow(2, evz)]
crossing=[khvnl,gkn]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_2_1_0.csv"))
nr_regular=4
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
