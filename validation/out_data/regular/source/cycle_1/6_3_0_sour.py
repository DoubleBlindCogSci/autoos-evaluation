from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
IT7gl3Bbb_W=['wWsddqrAY','hILzm','aVUbVYYhm','X(AhOV}92WFgm',Level('qAgNvRGMe',3),'zDiYDkye',"WW}qiwP~e"]
pSNLq=Factor('Clbl#yEkS',[IT7gl3Bbb_W[3],'gtVJUIWy',"PwCySm",Level('yfdXy',5),'eHsosCM9F{Ude',':y3myCEKIH',Level("VjOd",1)])
VcEiSHLw=Factor("kBy)_X4Hzqe",[Level('QcS',9),'aPBFuz',Level('tqzmGY22HJEB',5),Level("7EEOYi^EOMna8l",10),Level('kV#hdR',3),"OXgHrjGR;@nao"])
aIw3NVE6='ZZkDSRH ;Aypo'
HjPzCn2Aq="xOJ"
xkZXVlpt=['SDSIwiqI?JlFk',HjPzCn2Aq,'mkNGovUra2Xm',aIw3NVE6,Level("W[&MuToGOvq",9),"Pm|IQ",'wMXYVAGALX',Level("zb?yZ|yqDHlcRq",2)]
Yypl=Factor('o3KWHkza^OToog',xkZXVlpt)

### EXPERIMENT
design=[pSNLq,VcEiSHLw,Yypl]
crossing=[pSNLq,VcEiSHLw,Yypl]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir, "out_code_1/6_3_0_0.csv"))
nr_factors=3
nr_levels=6
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir, "out_code_2/6_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir, "result_sour.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir, "result_sour.csv"), index=False)