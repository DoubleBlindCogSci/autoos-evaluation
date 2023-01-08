from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
xyfFL=["uhUXnEXCs8HyfK","pvE!bQ>UONI6y","AnkCSis)xOlIC"]
nOdlgJp4=Factor(';pkr{EXiq',xyfFL)
IFqGrh=Factor('zdo',['Urj1gZikPN','MiU','U~d@SfnHGS'])
TtEuhEoTK7c=Factor('mF9KSYGW',['KYAxQO','Iry1Asyr; ;Gy',"DLJOkI"])

### EXPERIMENT
design=[nOdlgJp4,IFqGrh,TtEuhEoTK7c]
crossing=[nOdlgJp4,IFqGrh,TtEuhEoTK7c]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_3_0_0.csv"))
nr_factors=3
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)