from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
cQwDUL7pH=Factor('NsqqYlavrf1IlZ',["I%JSJ",'pZX',')RVRs',Level('a9UAMJLkr',2),"sSPdU{WU"])
U3_RWzK1S7=[Level("0UqUEcb",10),'DWirHPcUJVPR!a','YozSOPeMjrX',"arfwGArd","u k~De!X H"]
aIs6k=Factor(';yrmvG',U3_RWzK1S7)

### EXPERIMENT
design=[cQwDUL7pH,aIs6k]
crossing=[cQwDUL7pH,aIs6k]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_2_1_0.csv"))
nr_factors=2
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)