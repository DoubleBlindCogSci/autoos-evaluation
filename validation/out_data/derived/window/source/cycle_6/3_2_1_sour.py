from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mfrme = Factor("mfrme", ["joqydt","mobtn","kzjju","mevtp","crjhjs","wii"])
tnwi = Factor("tnwi", ["bvvwd","rqnix","courr","xwwdvb","kste","idonp"])
def qaylt(mfrme, tnwi):
     return "wii" == mfrme[0] and tnwi[-2] != "kste"
def xifu(mfrme, tnwi):
     return mfrme[0] != "wii" and  tnwi[-2] == "kste"
def nezdt(mfrme, tnwi):
     return (not mfrme[0] == "wii") and (not tnwi[-2] == "kste")
pwotnh = Factor("xlyjlo", [DerivedLevel("ztgo", Window(qaylt, [mfrme, tnwi],3)), DerivedLevel("rqcz", Window(xifu, [mfrme, tnwi],3)),DerivedLevel("qfujr", Window(nezdt, [mfrme, tnwi],3))])
### EXPERIMENT
design=[mfrme,tnwi,pwotnh]
crossing=[pwotnh]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)