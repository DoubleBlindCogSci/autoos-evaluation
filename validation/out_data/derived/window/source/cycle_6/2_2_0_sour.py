from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
orv = Factor("orv", ["ecf","ctx","ydzol","fry","tmjvn"])
umaucr = Factor("umaucr", ["ecf","ctx","ydzol","fry","tmjvn"])
fdcldf = Factor("fdcldf", ["ecf","ctx","ydzol","fry","tmjvn"])
def qcyk(orv, umaucr, fdcldf):
    return orv[-1] == umaucr[0] and orv[0] == fdcldf[-1]
def lwyy(orv, umaucr, fdcldf):
    return orv[-1] != umaucr[0] or orv[0] != fdcldf[-1]
iuc = DerivedLevel("ayso", Window(qcyk, [orv, umaucr, fdcldf],2))
fznamu = DerivedLevel("asl", Window(lwyy, [orv, umaucr, fdcldf],2))
ppj = Factor("nlgc", [iuc, fznamu])

### EXPERIMENT
design=[orv,umaucr,fdcldf,ppj]
crossing=[ppj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)