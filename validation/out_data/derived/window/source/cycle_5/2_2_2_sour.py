from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
dhrnfc = Factor("dhrnfc", ["dav","onhc","rpl","lmj","kxolk"])
exxlpg = Factor("exxlpg", ["dav","onhc","rpl","lmj","kxolk"])
hbrqgi = Factor("hbrqgi", ["dav","onhc","rpl","lmj","kxolk"])
def vwnse(dhrnfc, exxlpg, hbrqgi):
    return dhrnfc[-1] == exxlpg[-2] or dhrnfc[-2] == hbrqgi[-1]
def dvefb(dhrnfc, exxlpg, hbrqgi):
    return dhrnfc[-1] != exxlpg[-2] and not (dhrnfc[-2] == hbrqgi[-1])
zjha = Factor("vmgfeo", [DerivedLevel("dbuz", Window(vwnse, [dhrnfc, exxlpg, hbrqgi],3)), DerivedLevel("iztnz", Window(dvefb, [dhrnfc, exxlpg, hbrqgi],3))])
### EXPERIMENT
design=[dhrnfc,exxlpg,hbrqgi,zjha]
crossing=[zjha]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/2_2_2_0.csv"))
nr_input_factors=2
nr_output_levels=2
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/2_2_2_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)