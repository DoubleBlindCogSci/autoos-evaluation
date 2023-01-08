from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
kbj = Factor("kbj", ["jnhscz", "enmgky"])
npycyx = Factor("npycyx", ["xbz", "pjtbin"])
ltjqdz = Factor("ltjqdz", ["jnhscz", "enmgky"])
dbb = Factor("dbb", ["xbz", "pjtbin"])
tdpseh = Factor("tdpseh", ["zgn", "sfu"])
design=[kbj,npycyx,ltjqdz,dbb,tdpseh]
constraints=[AtLeastKInARow(3, tdpseh),MinimumTrials(26)]
crossing=[npycyx,tdpseh]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_0_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_0_2_0.csv"))
nr_regular=5
nr_derived=0
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
