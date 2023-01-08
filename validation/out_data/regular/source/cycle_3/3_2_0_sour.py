from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
tGVS9=Factor('Vp>JpTcEPpTvQ6',[Level("Exbj",4),"IaU",Level('WS0',4)])
Jl8nIEW3WM=['PJvPW','us~!@xvF',Level('I|?pdoQyWNXNO',2)]
fZ6LD=Factor('sKXkOx',Jl8nIEW3WM)

### EXPERIMENT
design=[tGVS9,fZ6LD]
crossing=[tGVS9,fZ6LD]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_factors=2
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)