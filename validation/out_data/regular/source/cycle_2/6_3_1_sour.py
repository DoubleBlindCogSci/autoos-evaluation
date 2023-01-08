from sourpea.primitives import *
from sourpea.util import *
import pandas as pd
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ClzxESGoy5=['F{DEHr!hkbu',"hwulG",Level("5fB",7),Level('g$Tw$|hD',4)]
WUsClyUxJ=Factor("QsiCS>NyiKOI",["u7SXgrVA","Hd6AZsP FXzpp","QvwsJ!LQQh^",ClzxESGoy5[3],Level('gkOA',8),"J91",'FyJIroW '])
qmgNRpFry=Factor("yVhWORI$ybTCAg",['qEFFZyBFt','[C8@TLkuV','NuvEuCcGONdo)',"ZWkLap&c|*","fG4JV","LKsyttOx#nmMW"])
LaQQ19=['cZEp<RcyYb3',Level('fAM',10),"cpthQgvUnDjnyW","nn^^Z0sUgEwJSs","4et","PPbXZyNzKamVf"]
OzNhfCyUQ9=Factor("wnyiy",["oOVc]WxP",LaQQ19[1],'mi}vqR8C[A',Level("D?vL*lPpIlXcoZ",6),Level('MtYptrglyal',4),"gUxcnoK",Level("#ozHPj%",2)])

### EXPERIMENT
design=[WUsClyUxJ,qmgNRpFry,OzNhfCyUQ9]
crossing=[WUsClyUxJ,qmgNRpFry,OzNhfCyUQ9]
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