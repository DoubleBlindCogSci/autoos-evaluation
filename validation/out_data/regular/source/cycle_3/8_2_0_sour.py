from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IsDbeqyJ7Hy=Factor('wFEZE#WUQ^t',[Level("S9Gz",9),"]uxfmS3bj}6e8J","ryhLbZLomRXrRH","S1UcMomU_r",Level("upmMsKYZ62P",1),'JFfOH0?yxI ',"WXXP",'dsQ7ezis~j'])
uTfi=["2URpZLt",Level("L7eW79tbVind",4),Level('gCXjuKd7EvLFDA',6),'9zTxCzUQSQd#q',"EEMHqfpV]","EgKs)uVRZmNws",'FanE','sN4tdjli]']
euzPM=Factor("QfmIuVqDqzptL",uTfi)

### EXPERIMENT
design=[IsDbeqyJ7Hy,euzPM]
crossing=[IsDbeqyJ7Hy,euzPM]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_2_0_0.csv"))
nr_factors=2
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)