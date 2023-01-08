from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iiyrcc = Factor("iiyrcc", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
tevaa = Factor("tevaa", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
uabdyq = Factor("uabdyq", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
def nmaz(iiyrcc, tevaa, uabdyq):
     return tevaa == iiyrcc
def gpxqg(iiyrcc, tevaa, uabdyq):
     return tevaa != iiyrcc and uabdyq == iiyrcc
def wlrka(iiyrcc, tevaa, uabdyq):
     return (not nmaz(iiyrcc, tevaa, uabdyq)) and (not iiyrcc == uabdyq)
qceb = Factor("ibv", [DerivedLevel("ivi", WithinTrial(nmaz, [iiyrcc, tevaa, uabdyq])), DerivedLevel("cbi", WithinTrial(gpxqg, [iiyrcc, tevaa, uabdyq])),DerivedLevel("nncbtr", WithinTrial(wlrka, [iiyrcc, tevaa, uabdyq]))])
### EXPERIMENT
design=[iiyrcc,tevaa,uabdyq,qceb]
crossing=[qceb]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)