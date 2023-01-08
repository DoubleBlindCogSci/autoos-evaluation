from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
myriv = Factor("myriv", ["rix","czbk","ryyilj","lmmecb","rungn","iex"])
def yuu(myriv):
     return "rix" == myriv[-2] and not myriv[0] == "rix"
def tby(myriv):
     return not "rix" == myriv[-2] and  myriv[0] == "czbk"
def igrk(myriv):
     return (myriv[-2] != "rix") and (not myriv[0] == "czbk")
igqfk = DerivedLevel("tkiu", Window(yuu, [myriv],3))
sgx = DerivedLevel("nxmsiz", Window(tby, [myriv],3))
etjki = DerivedLevel("nandlu", Window(igrk, [myriv],3))
nefg = Factor("jpu", [igqfk, sgx, etjki])

### EXPERIMENT
design=[myriv,nefg]
crossing=[nefg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)