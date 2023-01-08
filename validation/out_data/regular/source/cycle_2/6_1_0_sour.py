from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ouAk=['V|eCcW',"Vt:LhBYQ",'j9z',Level('VuIL>jwMLWPA8L',3),"mjeM6wMKYIK",Level("SDC",6),'OGgiFCbX',Level('fIRynxfuQO(',9),'tkF9[u*Cs&HjP']
WTW0SiRNb0g=Factor('9Hbo',[ouAk[4],"UqULnkQ_jBt",Level("ueEbBR$NX1kV}i",4),'X[nF$w;:g','tMGI','SGm',"FBovs"])

### EXPERIMENT
design=[WTW0SiRNb0g]
crossing=[WTW0SiRNb0g]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_1_0_0.csv"))
nr_factors=1
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_1_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)