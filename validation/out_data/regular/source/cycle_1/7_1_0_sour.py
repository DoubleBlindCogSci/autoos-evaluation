from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ctsfA7q='jdhGrna'
NwWK4Z3k=Factor("H#ymIW:&",[Level('qWFHHX:jFVOvX',3),'rNif',"TEFwkWzmYBth",ctsfA7q,Level('JVz',7),'2t&coV#X','ahT','FoyjlRy}Q~r'])

### EXPERIMENT
design=[NwWK4Z3k]
crossing=[NwWK4Z3k]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/7_1_0_0.csv"))
nr_factors=1
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/7_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)