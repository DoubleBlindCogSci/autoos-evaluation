from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
eB_zaL6=Factor('FRep',["kQEFiiw|6lz7",Level('fLMdM S',6)])
HbnveUld1ia=Factor('dqWvEw;1ke&f',['VcYd7Fh',"RPd9xPS"])
cJ1f8hbzJT1=['rrsZ',"MaocZJZr:KI"]
LsWqf0g7QN8=Factor('5HMqbAriUXtgR',cJ1f8hbzJT1)

### EXPERIMENT
design=[eB_zaL6,HbnveUld1ia,LsWqf0g7QN8]
crossing=[eB_zaL6,HbnveUld1ia,LsWqf0g7QN8]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_3_0_0.csv"))
nr_factors=3
nr_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)