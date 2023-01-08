from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vrq = Factor("vrq", ["dgxe","fngdhc","yreu","wbw","eizq","zhh"])
ouics = Factor("ouics", ["hvjfh","yoibhb","fuaex","aoc","xykbw","wunj"])
def bbrveh(vrq, ouics):
     return vrq == "eizq"
def bhsp(vrq, ouics):
     return "eizq" != vrq and  ouics == "wunj"
def rpb(vrq, ouics):
     return (not vrq == "eizq") and (ouics != "wunj")
gypmm = Factor("chd", [DerivedLevel("iim", WithinTrial(bbrveh, [vrq, ouics])), DerivedLevel("lkyk", WithinTrial(bhsp, [vrq, ouics])),DerivedLevel("eqe", WithinTrial(rpb, [vrq, ouics]))])
### EXPERIMENT
design=[vrq,ouics,gypmm]
crossing=[gypmm]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_3_0.csv"))
nr_input_factors=2
nr_output_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_3_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)