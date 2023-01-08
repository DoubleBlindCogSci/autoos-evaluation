from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
cyovro = Factor("cyovro", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
qoyk = Factor("qoyk", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
zjgjio = Factor("zjgjio", ["wbde","qnjs","lzto","yxvnmb","gsxfcz","zldecv","mdke"])
def sjxel(cyovro, qoyk, zjgjio):
     return qoyk[-1] == cyovro[0] and cyovro[-1] != zjgjio[0]
def axnc(cyovro, qoyk, zjgjio):
     return qoyk[-1] != cyovro[0] and cyovro[-1] == zjgjio[0]
def eykatp(cyovro, qoyk, zjgjio):
     return (not sjxel(cyovro, qoyk, zjgjio)) and (not cyovro[-1] == zjgjio[0])
afliw = DerivedLevel("pgc", Transition(sjxel, [cyovro, qoyk, zjgjio]))
qhw = DerivedLevel("efgfn", Transition(axnc, [cyovro, qoyk, zjgjio]))
nsi = DerivedLevel("avaxq", Transition(eykatp, [cyovro, qoyk, zjgjio]))
fho = Factor("qfzc", [afliw, qhw, nsi])

### EXPERIMENT
design=[cyovro,qoyk,zjgjio,fho]
crossing=[fho]
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