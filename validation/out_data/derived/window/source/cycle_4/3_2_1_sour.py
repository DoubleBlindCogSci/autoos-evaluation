from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
uqwxh = Factor("uqwxh", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
vwoe = Factor("vwoe", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
ckstue = Factor("ckstue", ["bixpkk","kkf","yjxjug","yurjl","asss","snqm","yjy","rssmp"])
def kzmmbm(uqwxh, ckstue, vwoe):
     return uqwxh[-3] == ckstue[0] and uqwxh[0] != vwoe[-3]
def uobo(uqwxh, ckstue, vwoe):
     return ckstue[0] != uqwxh[-3] and uqwxh[0] == vwoe[-3]
def cko(uqwxh, ckstue, vwoe):
     return (not kzmmbm(uqwxh, ckstue, vwoe)) and (not uobo(uqwxh, ckstue, vwoe))
uwai = DerivedLevel("mfqks", Window(kzmmbm, [uqwxh, vwoe, ckstue],4))
ndbbht = DerivedLevel("ifgsok", Window(uobo, [uqwxh, vwoe, ckstue],4))
rzpw = DerivedLevel("xywkiw", Window(cko, [uqwxh, vwoe, ckstue],4))
ehagiv = Factor("kjq", [uwai, ndbbht, rzpw])

### EXPERIMENT
design=[uqwxh,vwoe,ckstue,ehagiv]
crossing=[ehagiv]
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