from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xgtcl = Factor("xgtcl", ["whmbm","jnj","porzs","mph","sbjdi","hbz","ziya"])
def elho(xgtcl):
    return xgtcl[-1] == "sbjdi" or xgtcl[-2] == "ziya"
def ofohk(xgtcl):
    return not elho(xgtcl)
esghry = DerivedLevel("fkd", Window(elho, [xgtcl],3,1))
lreq = DerivedLevel("hnepud", Window(ofohk, [xgtcl],3,1))
tfahh = Factor("fpqvm", [esghry, lreq])

### EXPERIMENT
design=[xgtcl,tfahh]
crossing=[tfahh]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)