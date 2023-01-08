from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dnra = Factor("dnra", ["ljvmuk","ygt","rvrj","grjvgd","wbxeh","xnah"])
hxqdn = Factor("hxqdn", ["rpszlw","qcbwi","zfrk","hevlrn","bkjxw","jmtsrb","mln"])
def kbhic(dnra, hxqdn):
     return "xnah" == dnra[-1] and hxqdn[-3] != "hevlrn"
def txrqqf(dnra, hxqdn):
     return "xnah" != dnra[-1] and  hxqdn[-3] == "hevlrn"
def ybk(dnra, hxqdn):
     return (not dnra[-1] == "xnah") and (hxqdn[-3] != "hevlrn")
jnk = Factor("xyye", [DerivedLevel("cigu", Window(kbhic, [dnra, hxqdn],4)), DerivedLevel("lyc", Window(txrqqf, [dnra, hxqdn],4)),DerivedLevel("ewzu", Window(ybk, [dnra, hxqdn],4))])
### EXPERIMENT
design=[dnra,hxqdn,jnk]
crossing=[jnk]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_1_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)