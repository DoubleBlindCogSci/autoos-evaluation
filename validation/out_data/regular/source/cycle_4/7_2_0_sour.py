from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aCfhoIk=Factor("jHDCE",["InST:kxae",Level('MfLUPxpGszDb',4),'FtKxNdDtOn8dri','KOyK',"InZ|",'dhNtFzbwjDM}O','EvEKTf'])
L3uny=["(wvqjawd*mh",'ElzyZldi|FZyZ','Cs@','|_PKersD](jwpP',Level("kjgUIAlozFRoyt",1),Level("XeaJh?K",3),";laEhTQPABNh"]
uDiL=Factor('LztfSJW2H?WQy',L3uny)

### EXPERIMENT
design=[aCfhoIk,uDiL]
crossing=[aCfhoIk,uDiL]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_2_0_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)