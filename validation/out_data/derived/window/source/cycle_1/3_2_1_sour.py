from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
 ### DERIVED FACTORS
bsy = Factor("bsy", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
nopd = Factor("nopd", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
fhq = Factor("fhq", ["pccj","drl","bzlogf","qtctr","bsz","msu","itl"])
def vjzjb(bsy, nopd, fhq):
     return bsy[0] == nopd[-3]
def yst(bsy, nopd, fhq):
     return nopd[-3] != bsy[0] and fhq[0] == bsy[-3]
def ang(bsy, nopd, fhq):
     return (not vjzjb(bsy, nopd, fhq)) and (not yst(bsy, nopd, fhq))
esxqjs = DerivedLevel("xkn", Window(vjzjb, [bsy, nopd, fhq],4))
kza = DerivedLevel("bxvp", Window(yst, [bsy, nopd, fhq],4))
ferqf = DerivedLevel("ylwc", Window(ang, [bsy, nopd, fhq],4))
zzuvq = Factor("nsaqy", [esxqjs, kza, ferqf])

### EXPERIMENT
design=[bsy,nopd,fhq,zzuvq]
crossing=[zzuvq]
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
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], test_code_1["levels"], test_code_2["levels"], nr_input_factors, nr_output_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)