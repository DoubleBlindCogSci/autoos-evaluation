from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
rwkex = Factor("rwkex", ["ievjo","oaostz","uxhbc","hlyauw","lis","otcr"])
def jheukf(rwkex):
     return "hlyauw" == rwkex[0] and not rwkex[-1] == "lis"
def qgsbvq(rwkex):
     return (not "hlyauw" != rwkex[0]) and  "lis" == rwkex[-1]
def utl(rwkex):
     return (not rwkex[0] == "hlyauw") and (not rwkex[-1] == "lis")
ouxtg = DerivedLevel("ufpf", Transition(jheukf, [rwkex]))
hgnj = DerivedLevel("lrbn", Transition(qgsbvq, [rwkex]))
hep = DerivedLevel("mwop", Transition(utl, [rwkex]))
oqszcj = Factor("klc", [ouxtg, hgnj, hep])

### EXPERIMENT
design=[rwkex,oqszcj]
crossing=[oqszcj]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_4_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_4_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)