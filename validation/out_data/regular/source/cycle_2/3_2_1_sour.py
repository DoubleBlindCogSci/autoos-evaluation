from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bTW3=[Level('lyOOD[0U>uxX',3),Level('QSOx9Ljaxj',10),'kSg']
XDOSB=Factor("UN _V[2fs",bTW3)
tTIywLzB=[Level('EpXmH',10),Level("JlQX9",5),Level('R1#V',8)]
hIBf3skp=Factor('F9Q>XrOfyoLdMm',tTIywLzB)

### EXPERIMENT
design=[XDOSB,hIBf3skp]
crossing=[XDOSB,hIBf3skp]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)