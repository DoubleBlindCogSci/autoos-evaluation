from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
r1cT3mPbw=Factor("TpSyH",["qvv","~uZzSl",Level('~UX>Akw NFk',7),Level('ZXObQhL',4),"PXCmymqM<",Level('UpGGxXu% ',10),'pDBXfz','VyYSVwPgFac x_'])
_TBsM46xr=Level('cJnhg@jVoPlAO9',9)
fQAPXL8wRZ=['GuRaQE','iByNS',"5Wrmnt"]
Be07=["Sv?Q",Level("Y0lQ j#aT",4),Level('z^jVnIZC6k',7),"1i[c3IC",_TBsM46xr,"6eyaLcBL:vy@d|",'Hzd@WSISDdt2x',"@wjzxGHMxkh5",fQAPXL8wRZ[1],'NjQ)']
aRQrvO2UB=Factor("hoVgtgpKmVWe",Be07)
_FC1=[Level('Rsxk',3),Level("cdaQVimM",7),Level("GvMk",9),';sF0',"gvTmz_C0ByQAK","Zi;2rF@R",'g]nkKj','o;rGrZT8d']
zoEXXn=Factor('t$hSsEQ]nDHGxg',_FC1)

### EXPERIMENT
design=[r1cT3mPbw,aRQrvO2UB,zoEXXn]
crossing=[r1cT3mPbw,aRQrvO2UB,zoEXXn]
### APPENDIX
block=Block(design,crossing,[])
sequence_code_1=trials_from_csv(os.path.join(_dir,"out_code_1/8_3_0_0.csv"))
nr_factors=3
nr_levels=8
test_code_1=block.test(sequence_code_1)
try:
	sequence_code_2=trials_from_csv(os.path.join(_dir,"out_code_2/8_3_0_0.csv"))
	test_code_2=block.test(sequence_code_2)
except:
	test_code_2={"pValue":0}
df=pd.read_csv(os.path.join(_dir,"result_sour_c1.csv"))
df.loc[len(df.index)] = [test_code_1["pValue"], test_code_2["pValue"], nr_factors, nr_levels]
df.to_csv(os.path.join(_dir,"result_sour_c1.csv"), index=False)