from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
uaijwz = Factor("uaijwz", ["ekn","fzqg","szbai","pfoq","glg"])
def szlq(uaijwz):
    return uaijwz[0] == "glg" or uaijwz[-1] == "pfoq"
def vjk(uaijwz):
    return uaijwz[0] != "glg" and uaijwz[-1] != "pfoq"
iragz = DerivedLevel("oueuq", Transition(szlq, [uaijwz]))
gki = DerivedLevel("mriz", Transition(vjk, [uaijwz]))
aku = Factor("lnauvj", [iragz, gki])

### EXPERIMENT
design=[uaijwz,aku]
crossing=[aku]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)