from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
FuTAPyh=Factor("auEoRjOoUoY",['lc7xSZt',Level("rptBXcIX{M",6),"Agyby:hOe","r2eaF1AWHv",'YehMUHRE',"%nRB","HXdfaZaJfs","B;~Bz&GsKu"])
f7zz9_r="OMYRU"
n61YGoU=Factor(' Y1i',[Level('H}JQlKD9xLU',1),'x[IB',Level('N}K~LzJ0f',4),"oCs]",f7zz9_r,Level('wrNxwn',7),"ZaZsE",Level('knK)m!qFc',2),"Xhnf:npliL"])
rz8P=Factor("IDgrZeSAS6J",[Level("MinwE%Bkvxlm",1),'QFzszNUNw*aAo','NPbIlW',Level("FT~OSUKsC",1),Level('dZ;Q',5),'eHWbWphlpFg',' 0Oe',"ZEmL "])

### EXPERIMENT
design=[FuTAPyh,n61YGoU,rz8P]
crossing=[FuTAPyh,n61YGoU,rz8P]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_3_1_0.csv"))
nr_factors=3
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)