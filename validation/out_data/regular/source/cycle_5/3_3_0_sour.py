from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
OgO_n=['WFBYVeYkJhs&','gSe0BywImue;#',"!OhR6?fz"]
xG11xwGAke8=Factor('EBsKQ2',OgO_n)
EkOt0=['>Tovw[Uew',"SIpw","PNlzeIYhY>X"]
Ei2U6nTGzIm=Factor("Oo2OBMm",EkOt0)
Kc9momshHDO=Factor("qdKXKQT7",["gNkhqL;tr!G",'wmAo','XrwFO&Z;tDg'])

### EXPERIMENT
design=[xG11xwGAke8,Ei2U6nTGzIm,Kc9momshHDO]
crossing=[xG11xwGAke8,Ei2U6nTGzIm,Kc9momshHDO]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/3_3_0_0.csv"))
nr_factors=3
nr_levels=3
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/3_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour.csv"), index=False)