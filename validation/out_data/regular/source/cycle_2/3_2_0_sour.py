from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IncbFT=["uEQEp",'zngvOgjInkCCe',"TbrhwXKm:QrEsR"]
OBu1n=Factor("cBEra",IncbFT)
ZMcPvXKX="aZXs"
cSQdpL=['XYf&f gEMX1',ZMcPvXKX,"jQKqc",Level('X|G(',2)]
ixtXIjB3=Factor('yX>wc',cSQdpL)

### EXPERIMENT
design=[OBu1n,ixtXIjB3]
crossing=[OBu1n,ixtXIjB3]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_2_0_0.csv"))
nr_factors=2
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)