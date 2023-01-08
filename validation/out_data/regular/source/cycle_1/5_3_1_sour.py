from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qxVy48N0lw=Factor('hDgQWaXpJJ6Z',["Zqh)C1x",Level('mt]IDVYR@UZH',9),'fMKmyzbf','DELscRU#P|utl}','fC>DXcdXJQMjhm'])
gwa26ZWKC=Level("SNL",9)
df5WDh9McCW=Factor('wGgWr',[gwa26ZWKC,Level("FSH",1),"cxlmR",Level("enWvs]SdPQfU",2),Level('FMyr_g3lEfn',10),'pXBiAxc|'])
VmOWCt3=Factor("ynYzCPvL%mPs",['dQstz?fp)Um','CziVPGnK','Kpt',Level("kyhQSeMg",4),"jtcK"])

### EXPERIMENT
design=[qxVy48N0lw,df5WDh9McCW,VmOWCt3]
crossing=[qxVy48N0lw,df5WDh9McCW,VmOWCt3]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/5_3_1_0.csv"))
nr_factors=3
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/5_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)