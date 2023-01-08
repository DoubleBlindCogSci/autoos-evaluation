from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
dYRB=Factor("TqnSP",['pqgnyBtyR',Level("ZqWUWLTqt@Fggx",1),"AJ)"])
OOV9RYJC=[Level('aHL',4),'XpLoczwKvJY',"spIJDRGSc3"]
FSk8=Factor("5QOKNrcoyYWR",OOV9RYJC)

### EXPERIMENT
design=[dYRB,FSk8]
crossing=[dYRB,FSk8]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_factors=2
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)