from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
ptxf = Factor("ptxf", ["nsmjwr", "iqbzt"])
fthd = Factor("fthd", ["fuezsy", "ddldqs"])
lln = Factor("lln", ["nsmjwr", "iqbzt"])
lfcap = Factor("lfcap", ["fuezsy", "ddldqs"])
tku = Factor("tku", ["qupefs", "nbo"])
rvpgn = Factor("rvpgn", ["pysk", "ihgxhj"])
def ihy (lfcap, fthd):
    return lfcap == fthd
def jfenxo (lfcap, fthd):
    return not ihy(lfcap, fthd)
hjkr = Factor("hjkr", [DerivedLevel("xwex", WithinTrial(ihy, [lfcap, fthd])), DerivedLevel("cidq", WithinTrial(jfenxo, [lfcap, fthd]))])
design=[hjkr,ptxf,fthd,lln,lfcap,tku,rvpgn]
constraints=None
crossing=[fthd,tku]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_1_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_1_0_0.csv"))
nr_regular=6
nr_derived=1
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
