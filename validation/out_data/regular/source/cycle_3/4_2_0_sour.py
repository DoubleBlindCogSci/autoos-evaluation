from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ZYWlSe=[Level("UkGodpK",10),'XTl7;0ojFdtDkC',Level('fTjX',3),"rETujOKaOl"]
cXNJ1j0K=Factor('Houj;bCo$Do',ZYWlSe)
odjYrUj=Factor('CUA2WGwQ',['xJvBbqaal?LMUD',Level('Rrch?sDWbsC',7),'sytZkHy',Level("vAyCMFvWlmc}ef",5)])

### EXPERIMENT
design=[cXNJ1j0K,odjYrUj]
crossing=[cXNJ1j0K,odjYrUj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/4_2_0_0.csv"))
nr_factors=2
nr_levels=4
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/4_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)