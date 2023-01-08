from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
MsM4pS=[Level("srKtJYiwZr",3),"JO>ZDvyCgvMJB","cXsT$KKwLdBq","KqrbIo8eEo"]
XKN7=Factor("NjgQFJ",MsM4pS)
t65iPUYr=Factor('OFbEmU',['wjZfj',"lsH","gqeazvclevrST","FnH"])
l39CNLL="PIQ9JkUoOyII"
F6P9oJysU=Factor('?82Q^&IGtfRfZ',['uIaKxy;ptAK',"DycIbXUYN",Level('SVi',3),'Cjc|{Dua z',l39CNLL])

### EXPERIMENT
design=[XKN7,t65iPUYr,F6P9oJysU]
crossing=[XKN7,t65iPUYr,F6P9oJysU]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_3_0_0.csv"))
nr_factors=3
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)