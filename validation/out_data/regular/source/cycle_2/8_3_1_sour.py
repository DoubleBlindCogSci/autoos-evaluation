from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
RnXex=Factor("xwQGDVF",["Uko",'gO4iSNuT',Level("lRxrEeOEoIY",1),"&dVwiX",Level('mpM',4),Level("7lsu7Dsxp7ZsB",9),Level("NVwN",9),Level('8lqI;VSlnF!yK',4)])
YlA4Xus4=Level('yQbe!q}OuE;',8)
cuB6Dtq_41A=Level("yLC6wmxzi",4)
Qxusi1e8R4=Factor('iRabLm7ssv',[cuB6Dtq_41A,'pCw',"oVH3Mg|JwHrf",Level('klZF:YoOMK',3),'JDMNj',YlA4Xus4,Level("O:stSVaCELg",2),"drzYtM","uzY&NM Ts",Level('WZcPjpRX7ZB',7)])
Rj8IHi=Factor("ER vn99FM",['SOOR','hfDb8oO',Level("zxiBZ",10),"cJqEzja",'EQPbrTar%','fBizdUpK',Level('BuqtjEHrfD',9),"pKH"])

### EXPERIMENT
design=[RnXex,Qxusi1e8R4,Rj8IHi]
crossing=[RnXex,Qxusi1e8R4,Rj8IHi]
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