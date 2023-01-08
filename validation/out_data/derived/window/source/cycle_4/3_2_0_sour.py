from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iuuz = Factor("iuuz", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
pfwafi = Factor("pfwafi", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
dxcv = Factor("dxcv", ["qwvmh","keht","pfkmy","vdlw","sueuw","jahl"])
def qvk(iuuz, dxcv, pfwafi):
     return iuuz[0] == dxcv[-3] and iuuz[-3] != pfwafi[0]
def iabmzw(iuuz, dxcv, pfwafi):
     return dxcv[-3] != iuuz[0] and pfwafi[0] == iuuz[-3]
def hgyemc(iuuz, dxcv, pfwafi):
     return (not iuuz[0] == dxcv[-3]) and (iuuz[-3] != pfwafi[0])
hvya = DerivedLevel("uik", Window(qvk, [iuuz, pfwafi, dxcv],4))
duxon = DerivedLevel("rrqftz", Window(iabmzw, [iuuz, pfwafi, dxcv],4))
ciiwa = DerivedLevel("rxcigz", Window(hgyemc, [iuuz, pfwafi, dxcv],4))
sohqcv = Factor("ogak", [hvya, duxon, ciiwa])

### EXPERIMENT
design=[iuuz,pfwafi,dxcv,sohqcv]
crossing=[sohqcv]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)