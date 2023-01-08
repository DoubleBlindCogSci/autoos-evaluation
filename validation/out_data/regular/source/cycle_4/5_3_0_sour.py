from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
VM0QWHGsRc=['AguZe4q',"D)TCvHd",'LWL;bfUfMXX','~Hhtt3e|A',"oLUkOP"]
P6BfH3=Factor('kgo',VM0QWHGsRc)
KDqJZC='vHV$k?RA*O7Uyz'
lPnkFMjO=['Ex*R dnbSS5y',"N_5rUhhWxNAi","nDMnG","Hh2g hauQVdM",KDqJZC,'rjkGF*PW']
BFdVoJVy=Factor('K>m4KDLurXc',lPnkFMjO)
Mx83aGSd=Factor("ai2",[Level("WlYDRfsh",4),Level('uB|ULzZZimJWrw',3),'7&%>JRT',"FXSjvTIFCHi","hZUta"])

### EXPERIMENT
design=[P6BfH3,BFdVoJVy,Mx83aGSd]
crossing=[P6BfH3,BFdVoJVy,Mx83aGSd]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_0_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)