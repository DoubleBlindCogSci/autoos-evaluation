from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
xkj = Factor("xkj", ["ljiv","hitf","jctbq","savcm","gyed","cdrgmp","xynbu","anvp"])
def zbdf(xkj):
     return "savcm" == xkj
def hxqd(xkj):
     return "cdrgmp" == xkj
def twq(xkj):
     return (xkj != "savcm") and (xkj != "cdrgmp")
qzka = DerivedLevel("jshn", WithinTrial(zbdf, [xkj]))
ifve = DerivedLevel("ztvy", WithinTrial(hxqd, [xkj]))
dpvwra = DerivedLevel("enxao", WithinTrial(twq, [xkj]))
nlw = Factor("lssd", [qzka, ifve, dpvwra])

### EXPERIMENT
design=[xkj,nlw]
crossing=[nlw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_2_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)