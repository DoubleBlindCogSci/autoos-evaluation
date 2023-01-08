from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
aj23=Factor("H]3Gy",["McJ","YE0EljDOS8<b","fJN^j","an]h",'pxgSXj'])
mvPqr9=">niF"
hRnfCZCK1=Factor("gzSpe2rw(PJ",["kpCRry",mvPqr9,"KiJnnEXa",'dHvgkVbBzCA',Level("g6ZRiFTYaj^(",2),"HRsG>lTDj"])
GkfwI39fD=["BlMPCuo","FzIRczt","GmTEPBKPmI","YYsI",Level('MaXKUTYqmV1B~j',1)]
RG4QtmNLXm=Factor("IIL~qDzfFREA",GkfwI39fD)

### EXPERIMENT
design=[aj23,hRnfCZCK1,RG4QtmNLXm]
crossing=[aj23,hRnfCZCK1,RG4QtmNLXm]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_3_1_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)