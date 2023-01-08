from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
zgwty = Factor("zgwty", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
muz = Factor("muz", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
isi = Factor("isi", ["lrxps","evaz","dor","ncxhe","apsexc","hhcc","cbkgpp"])
def bwz(zgwty, isi, muz):
     return zgwty[0] == isi[-3] and zgwty[-3] != muz[0]
def xhuz(zgwty, isi, muz):
     return isi[-3] != zgwty[0] and zgwty[-3] == muz[0]
def aul(zgwty, isi, muz):
     return (not zgwty[0] == isi[-3]) and (not zgwty[-3] == muz[0])
hio = Factor("knehq", [DerivedLevel("lfnwwo", Window(bwz, [zgwty, muz, isi],4)), DerivedLevel("sdddpo", Window(xhuz, [zgwty, muz, isi],4)),DerivedLevel("vyjx", Window(aul, [zgwty, muz, isi],4))])
### EXPERIMENT
design=[zgwty,muz,isi,hio]
crossing=[hio]
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
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)