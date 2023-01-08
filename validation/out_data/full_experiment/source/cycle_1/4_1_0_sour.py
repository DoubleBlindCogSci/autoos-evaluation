from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### START
vsjz = Factor("vsjz", ["sjui", "ikecv"])
jko = Factor("jko", ["bqht", "weiurp"])
smcarz = Factor("smcarz", ["sjui", "ikecv"])
khud = Factor("khud", ["bqht", "weiurp"])
def wdoday (khud, vsjz):
    return khud == vsjz
def xcf (khud, vsjz):
    return not wdoday(khud, vsjz)
zwizsh = Factor("zwizsh", [DerivedLevel("inny", WithinTrial(wdoday, [khud, vsjz])), DerivedLevel("foini", WithinTrial(xcf, [khud, vsjz]))])
design=[zwizsh,vsjz,jko,smcarz,khud]
constraints=None
crossing=[smcarz,khud]
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/4_1_0_0.csv"))
sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/4_1_0_0.csv"))
nr_regular=4
nr_derived=1
nr_constraints=0
block = Block(design,crossing,constraints)
test_1 = block.test(sequence_code_1)
test_2 = block.test(sequence_code_2)
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_1["pValue"], test_2["pValue"], test_1["levels"], test_2["levels"], test_1["constraints"], test_2["constraints"],nr_regular, nr_derived, nr_constraints]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)
