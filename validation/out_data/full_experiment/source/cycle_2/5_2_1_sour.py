from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
hbqz = Factor("hbqz", ["zdmblf", "shmy"])
ryk = Factor("ryk", ["quezyq", "xxciv"])
foohw = Factor("foohw", ["zdmblf", "shmy"])
cduyr = Factor("cduyr", ["quezyq", "xxciv"])
mij = Factor("mij", ["lpy", "grlbm"])
def pqtfru (hbqz, foohw):
    return hbqz == foohw
def obd (hbqz, foohw):
    return not pqtfru(hbqz, foohw)
xflnlc = Factor("xflnlc", [DerivedLevel("ydbchl", WithinTrial(pqtfru, [hbqz, foohw])), DerivedLevel("yiu", WithinTrial(obd, [hbqz, foohw]))])
def xzvmu (cduyr, mij):
    return cduyr == mij
def ozo (cduyr, mij):
    return not xzvmu(cduyr, mij)
zoyn = Factor("zoyn", [DerivedLevel("lsolqn", WithinTrial(xzvmu, [cduyr, mij])), DerivedLevel("una", WithinTrial(ozo, [cduyr, mij]))])
design=[xflnlc,zoyn,hbqz,ryk,foohw,cduyr,mij]
constraints=[AtLeastKInARow(4, cduyr)]
crossing=[zoyn,hbqz]
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_1_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_1_0.csv"))
nr_regular=5
nr_derived=2
nr_constraints=1
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)
