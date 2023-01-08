from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
mokqh = Factor("mokqh", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
rzgi = Factor("rzgi", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
oilv = Factor("oilv", ["tuoig","fji","rstfj","xdimx","byiuw","bxcy","tnmeod","kpaelj"])
def tgaup(mokqh, rzgi, oilv):
     return mokqh == rzgi
def imvlj(mokqh, rzgi, oilv):
     return rzgi != mokqh and mokqh == oilv
def arpqcs(mokqh, rzgi, oilv):
     return (not mokqh == rzgi) and (mokqh != oilv)
mwmdzj = DerivedLevel("rypi", WithinTrial(tgaup, [mokqh, rzgi, oilv]))
jvv = DerivedLevel("uidd", WithinTrial(imvlj, [mokqh, rzgi, oilv]))
kuua = DerivedLevel("cww", WithinTrial(arpqcs, [mokqh, rzgi, oilv]))
pwnyi = Factor("vgos", [mwmdzj, jvv, kuua])

### EXPERIMENT
design=[mokqh,rzgi,oilv,pwnyi]
crossing=[pwnyi]
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