from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
oizuh = Factor("oizuh", ["tyyvj","pwv","jjxmu","ayr","mbeusd","qscz"])
phqwn = Factor("phqwn", ["yyn","tkv","atjtz","uvhn","gjbkxc","oan","ktvo","prma"])
def mfi(oizuh, phqwn):
     return oizuh == "ayr"
def wfk(oizuh, phqwn):
     return oizuh != "ayr" and  phqwn == "atjtz"
def kdrnwg(oizuh, phqwn):
     return (not mfi(oizuh, phqwn)) and (not wfk(oizuh, phqwn))
xlitka = DerivedLevel("wqrobh", WithinTrial(mfi, [oizuh, phqwn]))
elguk = DerivedLevel("fozlre", WithinTrial(wfk, [oizuh, phqwn]))
vzdduv = DerivedLevel("tqmxnq", WithinTrial(kdrnwg, [oizuh, phqwn]))
fbdq = Factor("wwxb", [xlitka, elguk, vzdduv])

### EXPERIMENT
design=[oizuh,phqwn,fbdq]
crossing=[fbdq]
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