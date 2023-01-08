from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
ptqz = Factor("ptqz", ["ris","hkeewa","htq","hqizy","zya","qudqay","bigo","ftgj"])
def ayaavv(ptqz):
     return "hqizy" == ptqz[0] and not ptqz[-1] == "hqizy"
def pjb(ptqz):
     return not "hqizy" == ptqz[0] and  ptqz[-1] == "qudqay"
def yetd(ptqz):
     return (not ptqz[0] == "hqizy") and (not pjb(ptqz))
sbd = Factor("vge", [DerivedLevel("dkhvb", Window(ayaavv, [ptqz],2)), DerivedLevel("xhb", Window(pjb, [ptqz],2)),DerivedLevel("wvdtqo", Window(yetd, [ptqz],2))])
### EXPERIMENT
design=[ptqz,sbd]
crossing=[sbd]
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