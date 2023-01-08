from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cnz = Factor("cnz", ["hbnnk","ftewb","lsdb","ysdk","hnod","gunqsj"])
def qzasuk(cnz):
     return cnz == "gunqsj"
def fwhu(cnz):
     return cnz == "ysdk"
def vtbbra(cnz):
     return (not qzasuk(cnz)) and (not fwhu(cnz))
ekic = Factor("zcvwuy", [DerivedLevel("zxh", WithinTrial(qzasuk, [cnz])), DerivedLevel("pio", WithinTrial(fwhu, [cnz])),DerivedLevel("wqzdn", WithinTrial(vtbbra, [cnz]))])
### EXPERIMENT
design=[cnz,ekic]
crossing=[ekic]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_1_3_0.csv"))
nr_input_factors=1
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_1_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)