from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
vbjxsn = Factor("vbjxsn", ["wdbc","vvqt","sgn","mkxoap","xetve","pauc","budg","vrisak"])
def qgrnb(vbjxsn):
     return vbjxsn[0] == "mkxoap" and not vbjxsn[-3] == "mkxoap"
def ilgjn(vbjxsn):
     return vbjxsn[0] != "mkxoap" and  vbjxsn[-3] == "sgn"
def lwhro(vbjxsn):
     return (vbjxsn[0] != "mkxoap") and (vbjxsn[-3] != "sgn")
lwgmn = DerivedLevel("jdxtz", Window(qgrnb, [vbjxsn],4))
nqen = DerivedLevel("odq", Window(ilgjn, [vbjxsn],4))
tzzes = DerivedLevel("dps", Window(lwhro, [vbjxsn],4))
qvuwl = Factor("vgjlr", [lwgmn, nqen, tzzes])

### EXPERIMENT
design=[vbjxsn,qvuwl]
crossing=[qvuwl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_1_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)