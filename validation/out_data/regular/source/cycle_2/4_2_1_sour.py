from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
DZHINRsjzV=Factor("fiFAZYEF7",[Level('n;u{',10),Level('}JStvuEbR',6),Level('ZVM',3),'Oq z^{KPRkVf'])
vQsC_=Factor('K MYI4SMfSMnLr',[Level("YyV~klXy!K8Xf",5),Level('G[N%:vgGnTw',10),"yXrWqW}4[",'|Pj'])

### EXPERIMENT
design=[DZHINRsjzV,vQsC_]
crossing=[DZHINRsjzV,vQsC_]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_1_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)