from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
kqs = Factor("kqs", ["tqou", "zqh"])
xmy = Factor("xmy", ["nepkz", "ntiaq"])
mvcr = Factor("mvcr", ["tqou", "zqh"])
bzowuv = Factor("bzowuv", ["nepkz", "ntiaq"])
abkw = Factor("abkw", ["uil", "kes"])
zeqtq = Factor("zeqtq", ["nhzv", "npofit"])
design=[kqs,xmy,mvcr,bzowuv,abkw,zeqtq]
constraints=[AtLeastKInARow(3, abkw),AtMostKInARow(2, bzowuv)]
crossing=[mvcr,xmy]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_0_2_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_0_2_0.csv"))
nr_regular=6
nr_derived=0
nr_constraints=2
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
