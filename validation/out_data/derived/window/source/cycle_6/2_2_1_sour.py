from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
gudpr = Factor("gudpr", ["tpxk","mzxlux","eneif","vxp","enjsv"])
iqmtg = Factor("iqmtg", ["ygi","hwpanh","bfkbl","smrsqk","qdfvn","ldgwb","xqni"])
def jqfs(gudpr, iqmtg):
    return gudpr[-1] != "mzxlux" and iqmtg[0] != "qdfvn"
def frmwzg(gudpr,iqmtg):
    return not jqfs(gudpr, iqmtg)
cggu = DerivedLevel("bizxs", Window(jqfs, [gudpr, iqmtg],2))
fise = DerivedLevel("jyvte", Window(frmwzg, [gudpr, iqmtg],2))
jqqg = Factor("htfb", [cggu, fise])

### EXPERIMENT
design=[gudpr,iqmtg,jqqg]
crossing=[jqqg]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)