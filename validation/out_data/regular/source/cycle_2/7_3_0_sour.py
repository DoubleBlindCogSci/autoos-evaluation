from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
YEzsA="j<QkW"
irsl1mvBinz=Factor("N6Bn",[Level("Ldm",4),'chrUvnM|ZQvCS',YEzsA,">4lT7",'vZHr','K2ghss<YwE[Q','Y8aTbwKWnph',Level("mrJ",9)])
wTaEYf7bF=' pUWH'
ytWI0=Factor("hfm_3",[Level('fsEF',6),wTaEYf7bF,Level("OTUOppP;VCi",3),"hdurS",Level('ISuXvoVCPDP',9),Level("Qu2",2),'#K#F}dLXUh&RI',"WFKa"])
ErC0q="MFdi8MQhP[G"
MSXaO8=Factor("uPdZ<ygZP",[ErC0q,'UijZHGvx',Level("fltZe^8IxXIR",2),'b(b7OhdQPuFKE','HOX6XppTGg','saLs{Ze8Bu$ ',"os>jNIjMK","8SOhj[hhC"])

### EXPERIMENT
design=[irsl1mvBinz,ytWI0,MSXaO8]
crossing=[irsl1mvBinz,ytWI0,MSXaO8]
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