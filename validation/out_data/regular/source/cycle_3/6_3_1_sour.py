from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vHVze=['<Pf',"FDMiXDRDQ#mwDO",'jcuyb2i?Hu']
pFEp="K@7N_q"
kfffL6f_3=['GDJDoHTiO<',"BmBERcRytWF","TR~OmrjLEscjK",pFEp,vHVze[0],"(TJ$KJ9cCjF",'sGLswZAxy',Level('qlKxBtKj',2)]
z5Od=Factor('e1c',kfffL6f_3)
Zu2rhM=Level("f DVVjHcThY2hs",10)
NetD=[Level("kWqbHkKZ[!F",7),"^xRG",Level("~M5i",7),"Cwa",Zu2rhM,Level("2jatR0pLGxmg",4),"&qp"]
kV91=Factor("DKsJ",NetD)
JbGQ5hBD5Gw=Factor('qKX',[Level("5gO",4),"lSmc",Level('0yf8d',9),'J8W4',Level("rqKuLWd",8),Level("I<!jFcLxZ",6)])

### EXPERIMENT
design=[z5Od,kV91,JbGQ5hBD5Gw]
crossing=[z5Od,kV91,JbGQ5hBD5Gw]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/6_3_1_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/6_3_1_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)