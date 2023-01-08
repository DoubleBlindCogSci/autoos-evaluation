from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
tgyp = Factor("tgyp", ["jvy","kamjzt","pxaz","fuboj","wsa","buisa","rekfxs"])
izn = Factor("izn", ["trh","blzzdh","vmc","jxwuke","wxn","iof","depihe"])
def wbmgo(tgyp, izn):
     return "wsa" == tgyp[-3] and not izn[0] == "vmc"
def hemil(tgyp, izn):
     return tgyp[-3] != "wsa" and  izn[0] == "vmc"
def tlsqyj(tgyp, izn):
     return (tgyp[-3] != "wsa") and (not hemil(tgyp, izn))
zdpoz = DerivedLevel("zvo", Window(wbmgo, [tgyp, izn],4))
kixks = DerivedLevel("fhvwfc", Window(hemil, [tgyp, izn],4))
ceb = DerivedLevel("bxig", Window(tlsqyj, [tgyp, izn],4))
ztiwqt = Factor("hxtank", [zdpoz, kixks, ceb])

### EXPERIMENT
design=[tgyp,izn,ztiwqt]
crossing=[ztiwqt]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_4_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)