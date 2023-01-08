from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vQJ2i5ae=Factor("IBDVkH",["vvp","MO<Y:2w9&L",'2uZqVCxLgF',"piWiEwOAGus",Level("yOXTOW",3),"xqO",Level("eOGELHT0npm",2),Level('u2n:lR',9),Level("YcDBOFK",7)])

### EXPERIMENT
design=[vQJ2i5ae]
crossing=[vQJ2i5ae]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/9_1_0_0.csv"))
nr_factors=1
nr_levels=9
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/9_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)