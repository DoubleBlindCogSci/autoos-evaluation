from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
pGYZq9k_R="z3o@a"
h_u8UsIbp4=['Exg[AC?ZBF&G',Level('LffPu',3),"k{Bsw:",pGYZq9k_R,Level(")gl",4),"mGH]feSN@E_wZ",'} SXCLk',"EpPGNSOMX|ID&",Level("w3JkLFy!ykO]",8)]
aEs8=Factor('z)T',h_u8UsIbp4)

### EXPERIMENT
design=[aEs8]
crossing=[aEs8]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/8_1_0_0.csv"))
nr_factors=1
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/8_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)