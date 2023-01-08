from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
hzss = Factor("hzss", ["ujnts", "jkw"])
kdzg = Factor("kdzg", ["xdrmxs", "asdgvm"])
axn = Factor("axn", ["ujnts", "jkw"])
cvf = Factor("cvf", ["xdrmxs", "asdgvm"])
djjd = Factor("djjd", ["vymblj", "sii"])
design=[hzss,kdzg,axn,cvf,djjd]
constraints=[AtLeastKInARow(4, axn)]
crossing=[cvf,hzss]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_0_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_0_1_0.csv"))
nr_regular=5
nr_derived=0
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
