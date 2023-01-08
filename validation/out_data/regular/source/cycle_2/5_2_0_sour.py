from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
wcom_J=['UUHMmNSxl',Level("VGHkg",4),"pbPOGOw"]
sCqH2Dl=Level('kTSZa?Gz',9)
E1pm0x=[Level("IQJL",10),'3&h)AV',wcom_J[0],Level("qrFthpS|tVeHWJ",6),'GGI5Fea',sCqH2Dl,Level('dXEpv#xE[inoJd',10)]
SNj4gEinO=Factor('IRFBTnR',E1pm0x)
xt6ly9=["zP%yvoiE?Bv)y",Level("cS&ThNN",6),"vPZpS",Level('qcZYKB',6),"RYc"]
lzBL=Factor("TPlnvC*",xt6ly9)

### EXPERIMENT
design=[SNj4gEinO,lzBL]
crossing=[SNj4gEinO,lzBL]
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