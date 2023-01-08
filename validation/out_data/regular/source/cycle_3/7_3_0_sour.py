from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
db5Uzw6=["rRxiqRvijWO",'TaVwXKOg8Dc',"Qb r<ai2bOAMA3","f;eDr",'vNdiWv',Level("GHrWJ#eCG}l9LR",9),Level("Hvuap",7)]
Wij1m=Factor("XqQI&BWrlDu>Pz",db5Uzw6)
LtBD=[Level("GIcBndwfp",3),"gENxv","II{(I","nBX2uSr{v","ksDKlX",Level('yMwP',5),Level("UZi",4)]
YeWMT3q=Factor("kWbbX?pmpLa",LtBD)
psJn_zMqnq=Factor('SRLeTbi',[Level("QXpmqmLEyd",4),Level('JiI',7),'@cntVPw#F F#N',"CIR",'mOcq',"plb{Wy#","T[pbrfa"])

### EXPERIMENT
design=[Wij1m,YeWMT3q,psJn_zMqnq]
crossing=[Wij1m,YeWMT3q,psJn_zMqnq]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/7_3_0_0.csv"))
nr_factors=3
nr_levels=7
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/7_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)