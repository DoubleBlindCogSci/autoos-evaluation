from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
inm = Factor("inm", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
qcbti = Factor("qcbti", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
rmwf = Factor("rmwf", ["bzsv","wiep","mmt","gxzl","qumrht","jyuu","qoyiba","xpffj"])
def tdiun(inm, rmwf, qcbti):
     return rmwf[-1] == inm[0] and inm[-1] != qcbti[0]
def zxxyds(inm, rmwf, qcbti):
     return rmwf[-1] != inm[0] and qcbti[0] == inm[-1]
def eci(inm, rmwf, qcbti):
     return (not tdiun(inm, rmwf, qcbti)) and (inm[-1] != qcbti[0])
mozvr = DerivedLevel("ovxpz", Window(tdiun, [inm, qcbti, rmwf],2))
dazbpb = DerivedLevel("ojx", Window(zxxyds, [inm, qcbti, rmwf],2))
vbgfp = DerivedLevel("akwq", Window(eci, [inm, qcbti, rmwf],2))
ujsl = Factor("reyloi", [mozvr, dazbpb, vbgfp])

### EXPERIMENT
design=[inm,qcbti,rmwf,ujsl]
crossing=[ujsl]
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
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)