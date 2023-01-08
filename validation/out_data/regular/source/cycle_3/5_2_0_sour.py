from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
njgu8eOcP=[Level('f_W]B<ZRuG',9),'rF]ZyO',"ctG:tUTxkTUNH*",'e|Kmp7hKAg0Bg']
iqyk=Level('fTd',1)
Z81FVfr=Factor('Tj2z',['vJLcHx','>a<Dstn',njgu8eOcP[3],'X:MifqeRNZxDL{',Level('MjfPLdhu',6),"ug(4)",iqyk])
Sl8qK3A1i=Factor(";DoQDv",[Level("xadYQNJsPQIE",9),Level("nPsPIw",7),"bIqzL",'ErKccNMuoym T{',Level("kvKzrxfWmLvzS",9)])

### EXPERIMENT
design=[Z81FVfr,Sl8qK3A1i]
crossing=[Z81FVfr,Sl8qK3A1i]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/5_2_0_0.csv"))
nr_factors=2
nr_levels=5
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/5_2_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)