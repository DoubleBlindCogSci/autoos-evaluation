from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
mogppw = Factor("mogppw", ["nsmj", "hbav"])
ygz = Factor("ygz", ["lloiv", "epic"])
jxmg = Factor("jxmg", ["nsmj", "hbav"])
zuxak = Factor("zuxak", ["lloiv", "epic"])
imj = Factor("imj", ["pkq", "aeiu"])
def djklo (zuxak, ygz):
    return zuxak == ygz
def prmecd (zuxak, ygz):
    return not djklo(zuxak, ygz)
iaf = Factor("iaf", [DerivedLevel("pgzwhl", WithinTrial(djklo, [zuxak, ygz])), DerivedLevel("acco", WithinTrial(prmecd, [zuxak, ygz]))])
design=[iaf,mogppw,ygz,jxmg,zuxak,imj]
constraints=[ExactlyKInARow(4, mogppw),MinimumTrials(27)]
crossing=[jxmg,zuxak]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_1_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_1_2_0.csv"))
nr_regular=5
nr_derived=1
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
