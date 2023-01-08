from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
WUWwS2sGkG=Factor('IFianaRLFw',["3lIxCbWtjU@aeK",'}G8%!p',"eYHU",'EXHIiw(myce',"ig8rwTRloZn",Level('dBGyaZKn 1I]vG',4),"t(E8iu"])
LvzzL_=['ZAr',"Kv9Z9kW",'s!}U',Level("VmWdiT",9),Level('QHesrX&5XnU',1),'m1wUnTbe']
j6oAUeNZRi=['DUz ucY1na','Zgog',"USMSw2g^Inr","GI]bN6"]
SFvE0hf=Factor("PGxfqfvHjV{",[j6oAUeNZRi[0],"fnJFR","]RMPX9sY{vQDm",'sS@Y','qDVMv',LvzzL_[1],'DlQG$LlMyh(f',"CIYBliC",Level('Mw@|qRC~z',8)])

### EXPERIMENT
design=[WUWwS2sGkG,SFvE0hf]
crossing=[WUWwS2sGkG,SFvE0hf]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/7_2_0_0.csv"))
nr_factors=2
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/7_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)